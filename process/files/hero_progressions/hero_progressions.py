from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class HeroProgressionsProcessor(JsonProcessor):
    def process_json(self, obj):
        hero_progressions = []
        for hero_progression_obj in obj["Progressions"].values():
            hero_progressions.append({
                "id": id_int64_str_to_hex(hero_progression_obj["DID"]["ID"]),
                "name": hero_progression_obj["DID"]["Name"],
                "values": [int(value_str) for value_str in hero_progression_obj["Entries"]],
            })
        return hero_progressions

    def description(self):
        return 'Progressions of values related to heroes'
