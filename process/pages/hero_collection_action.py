from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException
from files.util import convert_numbers


def to_property_name(stat_name):
    if stat_name.startswith("driven_"):
        return "property_" + stat_name[7:] + "_hero"
    return stat_name


class HeroCollectionActionProcessor(PageProcessor):
    def process(self):
        return {
            "actions": self._process_actions(),
            "max_influence": self._process_progression(
                "hero_collection_action_properties", "prog_max_influence_by_level"
            ),
            "influence_regen": self._process_progression(
                "hero_collection_action_properties", "prog_influence_regen_by_level"
            ),
            "hero_stars_requirement": self._process_progression(
                "hero_collection_action_progressions", "prog_hero_collection_level"
            ),
        }

    def _process_actions(self):
        actions = []
        for raw_action in self.iterate_files(["hero_collection_actions"]):
            try:
                actions.append(self._process_action(raw_action))
            except InsufficientDataException as e:
                print(e)
                continue
        return actions

    def _process_progression(self, file_id, progression_name):
        return convert_numbers(
            self.lookup_file(file_id, "name", progression_name)["values"]
        )

    def _process_action(self, raw_action):
        stat = self.lookup_file(
            "properties", "name", to_property_name(raw_action["property_name"])
        )
        action = {
            "id": raw_action["id"],
            "name": self.translate(raw_action["name_placeholder"]),
            "description": self.translate(raw_action["description_placeholder"]),
            "tag": raw_action["tag"],
            "stat": {
                "name": self.translate(stat["name_placeholder"]),
                "description": self.translate(stat["description_placeholder"]),
            },
            "buff": self._process_progression(
                "hero_collection_action_properties", raw_action["buff_progression_name"]
            ),
            "cooldown": self._process_progression(
                "hero_collection_action_progressions",
                raw_action["cooldown_progression_name"],
            ),
            "duration": self._process_progression(
                "hero_collection_action_progressions",
                raw_action["duration_progression_name"],
            ),
            "influence_cost": self._process_progression(
                "hero_collection_action_progressions",
                raw_action["incluence_cost_progression_name"],
            ),
            "level": self._process_progression(
                "hero_collection_action_progressions",
                raw_action["level_progression_name"],
            ),
        }
        if "num_uses_progression_name" in raw_action:
            action["num_uses"] = self._process_progression(
                "hero_collection_action_progressions",
                raw_action["num_uses_progression_name"],
            )
        return action
