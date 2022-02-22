from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex

EQUIPMENT_SLOT_NAMES = {
    "helmet",
    "chest",
    "pants",
    "boots",
    "ring",
    "weapon",
}


def equipment_progression_attributes(slot_progressions, slot_name):
    slot_key = "slot_" + slot_name[0].upper() + slot_name[1:]
    slot = next(filter(lambda s: s["EquipmentSlot"]["Name"]
                       == slot_key, slot_progressions))
    return {
        slot_name + "_id": id_int64_str_to_hex(slot["EquipmentProg"]["ID"]),
        slot_name + "_name": slot["EquipmentProg"]["Name"],
    }


class GearSetsProcessor(JsonProcessor):
    def process_json(self, obj):
        gear_sets = []
        for gear_set_id, gear_set_obj in obj["Objects"].items():
            gear_set_output = {
                "id": id_int64_str_to_hex(gear_set_id),
                "name": gear_set_obj["DID"]["Name"],
                "name_placeholder": gear_set_obj["Name"],
                "description_placeholder": gear_set_obj["Description"],
                "priority": gear_set_obj["SortPriority"],
                "color": gear_set_obj["BackgroundColor"],
                "material_id": id_int64_str_to_hex(gear_set_obj["Material"]["ID"]),
                "material_name": gear_set_obj["Material"]["Name"],
            }
            for slot_name in EQUIPMENT_SLOT_NAMES:
                gear_set_output.update(
                    equipment_progression_attributes(gear_set_obj["SlotProgs"], slot_name))
            gear_sets.append(gear_set_output)
        return sorted(gear_sets, key=lambda g: g["priority"])

    def description(self):
        return 'Basic information about an event armory gear set'
