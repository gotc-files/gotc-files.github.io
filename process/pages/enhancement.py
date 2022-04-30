from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException


class EnhancementProcessor(PageProcessor):
    def process(self):
        enhancements = []
        for raw_enhancement in self.iterate_files(["buildings"]):
            if not raw_enhancement["enhancement_related_building"]:
                continue
            try:
                enhancements.append(self._process_enhancement(raw_enhancement))
            except InsufficientDataException as e:
                print(e)
                continue
        return enhancements

    def _process_enhancement(self, raw_enhancement):
        enhancement_stat = self.lookup_file(
            "building_stat_sets", "name", raw_enhancement["name"].lower())["stats"][0]
        power_progression = self.lookup_file(
            "enhancement_progressions", "name", raw_enhancement["power_progression"])["values"]
        event_score_progression = self.lookup_file(
            "event_scoring_progressions", "name", raw_enhancement["event_score_progression"])["values"]
        stat_progression = self.lookup_files(
            ["enhancement_progressions"], "name", enhancement_stat["progression"])["values"]
        upgrade_time_progression = self.lookup_file(
            "enhancement_progressions", "name", raw_enhancement["upgrade_time_progression"])["values"]
        cost_progressions = [(cost_entry["item_name"], self.lookup_file(
            "enhancement_progressions", "name", cost_entry["progression"])["values"]) for cost_entry in raw_enhancement["costs"]]

        return {
            "id": raw_enhancement["id"],
            "building": self.translate(
                self.lookup_file(
                    "buildings", "name", raw_enhancement["enhancement_related_building"])
                ["name_placeholder"]),
            "name": self.translate(raw_enhancement["name_placeholder"]),
            "description": self.translate(raw_enhancement["description_placeholder"]),
            "stat": self._process_enhancement_stat(enhancement_stat["name"]),
            "levels": [self._process_enhancement_level(
                i,
                power_progression[i],
                event_score_progression[i],
                stat_progression[i],
                upgrade_time_progression[i],
                [self._process_item_cost(item_name, cost_values[i])
                 for item_name, cost_values in cost_progressions],
            ) for i in range(len(event_score_progression))]
        }

    def _process_enhancement_level(self, index, power, event_score, stat, upgrade_time, costs):
        return {
            "level": index + 1,
            "power": power,
            "event_score": event_score,
            "stat": stat,
            "upgrade_time_seconds": upgrade_time,
            "costs": costs,
        }

    def _process_enhancement_stat(self, stat_name):
        stat = self.lookup_file("properties", "name", stat_name)
        return {
            "name": self.translate(stat["name_placeholder"]),
            "description": self.translate(stat["description_placeholder"]),
        }

    def _process_item_cost(self, item_name, cost):
        item = self.lookup_file("items", "name", item_name)
        return {
            "name": self.translate(item["name_placeholder"]),
            "description": self.translate(item["description_placeholder"]),
            "cost": cost,
        }
