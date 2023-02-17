from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException
from files.util import convert_numbers


PIECE_NAMES = ["ring", "weapon", "boots", "pants", "helmet", "chest"]


def _color_to_rgb(color):
    return "#" + "".join(
        [("%02x" % color.get(key, 0)) for key in ("red", "green", "blue")]
    )


class ArmoryProcessor(PageProcessor):
    def process(self):
        armory_sets = []
        for raw_armory_set in self.iterate_files(["gear_set_1", "gear_set_2"]):
            if any(
                [
                    (piece_name + "_name") not in raw_armory_set
                    for piece_name in PIECE_NAMES
                ]
            ):
                continue
            try:
                armory_sets.append(self._process_armory_set(raw_armory_set))
            except InsufficientDataException:
                continue
        return armory_sets

    def _process_armory_set(self, raw_armory_set):
        armory_collection = self.lookup_files(
            ["armory_collections_1", "armory_collections_2"],
            "gear_set_name",
            raw_armory_set["name"],
        )
        armory_set = {
            "id": raw_armory_set["id"],
            "name": self.translate(raw_armory_set["name_placeholder"]),
            "description": self.translate(raw_armory_set["description_placeholder"]),
            "material_name": self.translate(
                self.lookup_file("items", "name", raw_armory_set["material_name"])[
                    "name_placeholder"
                ]
            ),
            "color": _color_to_rgb(raw_armory_set["color"]),
        }
        for piece_name in PIECE_NAMES:
            armory_set[piece_name] = self._process_gear_piece(
                raw_armory_set[piece_name + "_name"]
            )

        for i in range(3):
            armory_set["bonus_" + str(i + 1)] = self._process_armory_stat(
                armory_collection["bonuses"][i]
            )

        return armory_set

    def _process_gear_piece(self, gear_piece_name):
        gear = self.lookup_files(
            ["gear_set_progressions_1", "gear_set_progressions_2"],
            "name",
            gear_piece_name,
        )
        if not gear:
            raise InsufficientDataException()
        return {
            "gear_with_level": list(
                map(
                    lambda gear_name_with_level: self._process_gear_with_level(
                        gear_name_with_level
                    ),
                    gear["gear_names_with_level"],
                )
            )
        }

    def _process_armory_stat(self, armory_stat_name):
        armory_stat = self.lookup_files(
            ["armory_stat_sets_1", "armory_stat_sets_2"],
            "name",
            armory_stat_name.lower(),
        )["stats"][0]
        return {
            "name": self.translate(
                self.lookup_file("properties", "name", armory_stat["name"])[
                    "name_placeholder"
                ]
            ),
            "description": self.translate(
                self.lookup_file("properties", "name", armory_stat["name"])[
                    "description_placeholder"
                ]
            ),
            "progression": convert_numbers(
                self.lookup_file(
                    "armory_stat_progressions", "name", armory_stat["progression"]
                )["values"]
            ),
        }

    def _process_gear_with_level(self, gear_name_with_level):
        gear_with_level = self.lookup_files(
            ["gears_1", "gears_2"], "name", gear_name_with_level
        )
        gear_stat_set = self.lookup_files(
            ["gear_stat_sets_1", "gear_stat_sets_2"], "name", gear_name_with_level
        )
        return {
            "name": gear_with_level["name"],
            "name": self.translate(gear_with_level["name_placeholder"]),
            "level": gear_with_level["level"],
            "stats": list(
                map(
                    lambda stat: self._process_gear_stat(
                        stat["name"], stat["progression"]
                    ),
                    gear_stat_set["stats"],
                )
            ),
        }

    def _process_gear_stat(self, stat_name, stat_progression_name):
        stat_progression = self.lookup_file(
            "gear_stat_progressions", "name", stat_progression_name
        )
        return {
            "name": self.translate(
                self.lookup_file("properties", "name", stat_name)["name_placeholder"]
            ),
            "description": self.translate(
                self.lookup_file("properties", "name", stat_name)[
                    "description_placeholder"
                ]
            ),
            "progression": convert_numbers(stat_progression["values"]),
        }
