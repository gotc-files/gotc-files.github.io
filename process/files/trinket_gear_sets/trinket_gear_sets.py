from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class TrinketGearSetsProcessor(JsonProcessor):
    def process_json(self, obj):
        trinket_gear_sets = []
        for trinket_gear_set_obj in obj["Objects"].values():
            trinket_gear_sets.append({
                "id": id_int64_str_to_hex(trinket_gear_set_obj["DID"]["ID"]),
                "name": trinket_gear_set_obj["DID"]["Name"],
                "name_placeholder": trinket_gear_set_obj["Name"],
                "description_placeholder": trinket_gear_set_obj["Description"],
                "priority": trinket_gear_set_obj["SortPriority"],
                "color": trinket_gear_set_obj["BackgroundColor"],
                "trinket_names": list(map(
                    lambda slot_prog: slot_prog["EquipmentProg"]["Name"], trinket_gear_set_obj["SlotProgs"])),
            })
        return sorted(trinket_gear_sets, key=lambda g: g["priority"])

    def description(self):
        return 'Basic information about a trinket gear set'
