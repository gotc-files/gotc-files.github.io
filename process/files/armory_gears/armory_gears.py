from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class ArmoryGearsProcessor(JsonProcessor):
    def process_json(self, obj):
        armory_gears = []
        for armory_gear_obj in obj["Objects"].values():
            armory_gears.append({
                "id": id_int64_str_to_hex(armory_gear_obj["DID"]["ID"]),
                "name": armory_gear_obj["DID"]["Name"].lower(),
                "armory_collection_name": armory_gear_obj["ArmoryCollection"]["Name"],
                "score_progression_name": armory_gear_obj["ScoreProg"]["Name"],
            })
        return armory_gears

    def description(self):
        return 'Gears/Trinkets to armory collection'
