from files.proto_processor import ProtoProcessor
from files.util import id_int64_to_hex
from files.gear_sets.gear_sets_pb2 import GearSets

EQUIPMENT_SLOT_NAMES = {
    "helmet",
    "chest",
    "pants",
    "boots",
    "ring",
    "weapon",
}


class GearSetsProcessor(ProtoProcessor):
    def proto_template(self):
        return GearSets()

    def process_proto(self, gear_sets):
        gear_sets_output = []
        for gear_set in gear_sets.gear_sets:
            gear_set_output = {
                "id": id_int64_to_hex(gear_set.identity.id),
                "name": gear_set.identity.name,
                "name_placeholder": gear_set.info.name_placeholder,
                "description_placeholder": gear_set.info.description_placeholder,
                "priority": gear_set.info.priority,
                "color": {
                    "red": gear_set.info.color.red,
                    "green": gear_set.info.color.green,
                    "blue": gear_set.info.color.blue,
                    "alpha": gear_set.info.color.alpha,
                },
            }
            if gear_set.info.material.id:
                gear_set_output.update(
                    {
                        "material_id": gear_set.info.material.id,
                        "material_name": gear_set.info.material.name,
                    }
                )
            for slot in gear_set.info.slots:
                slot_name = slot.slot.name[5:].lower()
                if slot_name in EQUIPMENT_SLOT_NAMES:
                    gear_set_output.update(
                        {
                            slot_name
                            + "_id": id_int64_to_hex(slot.gear_progression.id),
                            slot_name + "_name": slot.gear_progression.name,
                        }
                    )
                if slot.slot.name == "slot_Trinket":
                    if "trinket_names" not in gear_set_output:
                        gear_set_output["trinket_names"] = []
                    gear_set_output["trinket_names"].append(slot.gear_progression.name)
            gear_sets_output.append(gear_set_output)
        return sorted(gear_sets_output, key=lambda g: g["priority"])

    def description(self):
        return "Basic information about an event armory gear set"
