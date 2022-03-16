from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class ArmoryCollectionsProcessor(JsonProcessor):
    def process_json(self, obj):
        armory_collections = []
        for armory_collection_id, armory_collection_obj in obj["Objects"].items():
            armory_collection = {
                "id": id_int64_str_to_hex(armory_collection_id),
                "name": armory_collection_obj["DID"]["Name"],
                "name_placeholder": armory_collection_obj["CollectionName"],
                "gear_set_name": armory_collection_obj["AssociatedGearset"]["Name"],
                "priority": armory_collection_obj["SortPriority"],
                "bonuses": []
            }
            for bonus_obj in armory_collection_obj["Bonuses"]:
                armory_collection["bonuses"].append(bonus_obj["DID"]["Name"])
            armory_collections.append(armory_collection)

        return sorted(armory_collections, key=lambda g: g["priority"])

    def description(self):
        return 'Armory collection information'

    def key_name(self):
        return 'gear_set_name'
