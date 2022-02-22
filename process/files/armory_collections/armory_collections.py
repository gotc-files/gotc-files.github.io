from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class ArmoryCollectionsProcessor(JsonProcessor):
    def process_json(self, obj):
        armory_collections = []
        for armory_collection_id, armory_collection_obj in obj["Objects"].items():
            armory_collections.append({
                "id": id_int64_str_to_hex(armory_collection_id),
                "name": armory_collection_obj["DID"]["Name"],
                "name_placeholder": armory_collection_obj["CollectionName"],
                "gear_set_name": armory_collection_obj["AssociatedGearset"]["Name"],
                "priority": armory_collection_obj["SortPriority"],
                "bonus_1_name": armory_collection_obj["Bonuses"][0]["DID"]["Name"],
                "bonus_2_name": armory_collection_obj["Bonuses"][1]["DID"]["Name"],
                "bonus_3_name": armory_collection_obj["Bonuses"][2]["DID"]["Name"],
            })
        return sorted(armory_collections, key=lambda g: g["priority"])

    def description(self):
        return 'Armory collection information'

    def key_name(self):
        return 'gear_set_name'
