from collections import OrderedDict
from hashlib import md5

from files.util import convert_numbers
from pages.page_processor import InsufficientDataException, PageProcessor

PIECE_NAMES = [
    "saddle",
    "chanfron",
    "peytral",
]


def _color_to_rgb(color):
    return "#" + "".join(
        [("%02x" % color.get(key, 0)) for key in ("red", "green", "blue")]
    )

def name_to_id(name):
    return md5(name.encode('utf-8')).hexdigest()[-16:]


class DragonGearProcessor(PageProcessor):
    def process(self):
        return self._process_legacy() + self._process()

    def _process(self):
        dragon_gear_sets_dict = OrderedDict()
        for raw_dragon_gears in self.iterate_file("dragon_gears"):
            gear_name = raw_dragon_gears["name"]
            gear_set_name = gear_name.split("_")[3]
            gear_piece_name = raw_dragon_gears["slot_name"][5:].lower()
            if gear_set_name not in dragon_gear_sets_dict:
                id = name_to_id(gear_set_name)
                dragon_gear_sets_dict[gear_set_name] = {
                    "id": id,
                    "name": "n:" + gear_set_name,
                    "description": "n:",
                    "color": "#" + id[-6:],
                }
                for piece_name in PIECE_NAMES:
                    dragon_gear_sets_dict[gear_set_name][piece_name] = {
                        "gear_with_level": []
                    }
            dragon_gear_sets_dict[gear_set_name][gear_piece_name]["gear_with_level"].append(self._process_gear_with_level(gear_name))

        return list(dragon_gear_sets_dict.values())

    def _process_legacy(self):
        dragon_gear_sets = []
        for raw_dragon_gear_set in self.iterate_files(["gear_set_1", "gear_set_2"]):
            if any(
                [
                    (piece_name + "_name") not in raw_dragon_gear_set
                    for piece_name in PIECE_NAMES
                ]
            ):
                continue
            try:
                dragon_gear_sets.append(
                    self._process_dragon_gear_set(raw_dragon_gear_set)
                )
            except InsufficientDataException:
                continue
         
        return dragon_gear_sets
    


    def _process_dragon_gear_set(self, raw_dragon_gear_set):
        dragon_gear_set = {
            "id": raw_dragon_gear_set["id"],
            "name": self.translate(raw_dragon_gear_set["name_placeholder"]),
            "description": self.translate(
                raw_dragon_gear_set["description_placeholder"]
            ),
            "material_name": self.translate(
                self.lookup_file("items", "name", raw_dragon_gear_set["material_name"])[
                    "name_placeholder"
                ]
            ),
            "color": _color_to_rgb(raw_dragon_gear_set["color"]),
        }
        for piece_name in PIECE_NAMES:
            dragon_gear_set[piece_name] = self._process_gear_piece(
                raw_dragon_gear_set[piece_name + "_name"]
            )

        return dragon_gear_set

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

    def _process_gear_with_level(self, gear_name_with_level):
        gear_with_level = self.lookup_files(
            ["gears_1", "gears_2", "dragon_gears"], "name", gear_name_with_level
        )
        gear_stat_set = self.lookup_files(
            ["gear_stat_sets_1", "gear_stat_sets_2", "dragon_gear_stat_sets"], "name", gear_name_with_level
        )
        return {
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
