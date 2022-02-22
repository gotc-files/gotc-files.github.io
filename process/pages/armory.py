def _color_to_rgb(color):
    return '#' + ''.join([('%02x' % color.get(key, 0)) for key in ("red", "green", "blue")])


class InsufficientDataException(Exception):
    pass


class ArmoryProcessor:
    def __init__(self, file_data_dict):
        self.file_data_dict = file_data_dict

    def translate(self, key):
        translation = self.lookup_file('translations', key)
        if not translation:
            raise InsufficientDataException
        return translation

    def lookup_file(self, file_id, key):
        return self.lookup_files([file_id], key)

    def lookup_files(self, file_ids, key):
        for file_id in file_ids:
            if file_id not in self.file_data_dict:
                raise KeyError('File id %s invalid')
            if key in self.file_data_dict[file_id]:
                return self.file_data_dict[file_id][key]
        return None

    def iterate_files(self, file_ids):
        for file_id in file_ids:
            yield from self.iterate_file(file_id)

    def iterate_file(self, file_id):
        if file_id not in self.file_data_dict:
            raise KeyError('File id %s invalid')
        for value in self.file_data_dict[file_id]:
            yield value

    def process(self):
        armory_sets = []
        for raw_armory_set in self.iterate_files(['gear_set_1', 'gear_set_2']):
            try:
                armory_sets.append(self._process_armory_set(raw_armory_set))
            except InsufficientDataException:
                continue
        return armory_sets

    def _process_armory_set(self, raw_armory_set):
        armory_collection = self.lookup_files(
            ['armory_collections_1', 'armory_collections_2'], raw_armory_set['name'])
        return {
            "id": raw_armory_set["id"],
            "name": self.translate(raw_armory_set["name_placeholder"]),
            "description": self.translate(raw_armory_set["description_placeholder"]),
            "material_name": self.translate(self.lookup_file("items", raw_armory_set["material_name"])["name_placeholder"]),
            "color": _color_to_rgb(raw_armory_set["color"]),
            "ring": self._process_gear_piece(raw_armory_set["ring_name"]),
            "weapon": self._process_gear_piece(raw_armory_set["weapon_name"]),
            "boots": self._process_gear_piece(raw_armory_set["boots_name"]),
            "pants": self._process_gear_piece(raw_armory_set["pants_name"]),
            "helmet": self._process_gear_piece(raw_armory_set["helmet_name"]),
            "chest": self._process_gear_piece(raw_armory_set["chest_name"]),
            "bonus_1": self._process_armory_stat(armory_collection["bonus_1_name"]),
            "bonus_2": self._process_armory_stat(armory_collection["bonus_2_name"]),
            "bonus_3": self._process_armory_stat(armory_collection["bonus_3_name"]),
        }

    def _process_gear_piece(self, gear_piece_name):
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

    def _process_armory_stat(self, armory_stat_name):
        armory_stat = self.lookup_files(
            ['armory_stat_sets_1', 'armory_stat_sets_2'], armory_stat_name)
        return {
            "name": self.translate(self.lookup_file("properties", armory_stat["property"])["name_placeholder"]),
            "description": self.translate(self.lookup_file("properties", armory_stat["property"])["description_placeholder"]),
            "progression": self.lookup_file('armory_stat_progressions', armory_stat['progression'])["stats"]
        }

    def _process_gear_with_level(self, gear_name_with_level):
        gear_with_level = self.lookup_files(
            ["gears_1", "gears_2"], gear_name_with_level)
        gear_stat_set = self.lookup_files(
            ["gear_stat_sets_1", "gear_stat_sets_2"], gear_name_with_level)
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
