from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException


def _color_to_rgb(color):
    return '#' + ''.join([('%02x' % color.get(key, 0)) for key in ("red", "green", "blue")])


class TrinketArmoryProcessor(PageProcessor):

    def process(self):
        trinket_armory_sets = []
        for raw_trinket_armory_set in self.iterate_file('trinket_gear_sets'):
            try:
                trinket_armory_sets.append(
                    self._process_trinket_armory_set(raw_trinket_armory_set))
            except InsufficientDataException as e:
                print('Cannot process trinket armory set: %s because of %s' %
                      (raw_trinket_armory_set["name"], e))
                continue
        return trinket_armory_sets

    def _process_trinket_armory_set(self, raw_trinket_armory_set):
        trinket_armory_collection = self.lookup_files(
            ['armory_collections_1', 'armory_collections_2'], raw_trinket_armory_set['name'])
        trinkets = []
        for trinket_name in raw_trinket_armory_set["trinket_names"]:
            try:
                trinkets.append(self._process_trinket(trinket_name))
            except InsufficientDataException as e:
                print('Cannot process trinket with name: %s because of %s' %
                      (trinket_name, e))
                continue
        bonuses = []
        for bonus_name in trinket_armory_collection["bonuses"]:
            try:
                bonuses.append(self._process_bonus(bonus_name))
            except InsufficientDataException as e:
                print('Cannot process bonus with name: %s because of %s' %
                      (bonus_name, e))
                continue
        return {
            "id": raw_trinket_armory_set["id"],
            "name": self.translate(trinket_armory_collection["name_placeholder"]),
            "color": _color_to_rgb(raw_trinket_armory_set["color"]),
            "trinkets": trinkets,
            "bonuses": bonuses
        }

    def _process_trinket(self, gear_piece_name):
        gear = self.lookup_files(
            ["gear_set_progressions_1", "gear_set_progressions_2"], gear_piece_name)
        if not gear:
            raise InsufficientDataException()
        return {
            "gear_with_level": list(map(
                lambda gear_name_with_level: self._process_gear_with_level(
                    gear_name_with_level),
                gear["gear_names_with_level"]))
        }

    def _process_bonus(self, bonus_name):
        armory_stat = self.lookup_files(
            ['armory_stat_sets_1', 'armory_stat_sets_2'], bonus_name)
        return {
            "name": self.translate(self.lookup_file("properties", armory_stat["property"])["name_placeholder"]),
            "description": self.translate(self.lookup_file("properties", armory_stat["property"])["description_placeholder"]),
            "progression": self.lookup_file('armory_stat_progressions', armory_stat['progression'])["stats"]
        }

    def _process_gear_with_level(self, gear_name_with_level):
        gear_with_level = self.lookup_files(
            ["gears_1", "gears_2", "trinket_gears"], gear_name_with_level)
        if not gear_with_level:
            raise InsufficientDataException(
                'Gear %s does not exist' % gear_name_with_level)
        gear_stat_set = self.lookup_files(
            ["gear_stat_sets_1", "gear_stat_sets_2", "trinket_gear_stat_sets"], gear_name_with_level)
        if not gear_stat_set:
            raise InsufficientDataException(
                'Gear stat set %s does not exist' % gear_name_with_level)
        return {
            "name": gear_with_level["name"],
            "name": self.translate(gear_with_level["name_placeholder"]),
            "level": gear_with_level["level"],
            "stats": list(map(
                lambda stat: self._process_gear_stat(
                    stat["name"], stat["progression"]),
                gear_stat_set["stats"]))
        }

    def _process_gear_stat(self, stat_name, stat_progression_name):
        stat_progression = self.lookup_file(
            "gear_stat_progressions", stat_progression_name)
        return {
            "name": self.translate(self.lookup_file("properties", stat_name)["name_placeholder"]),
            "description": self.translate(self.lookup_file("properties", stat_name)["description_placeholder"]),
            "progression": stat_progression["stats"]
        }
