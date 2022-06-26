from files.unified_processor import UnifiedProcessor
from files.gears.gears_pb2 import Gears
from files.util import id_int64_to_hex
from files.util import id_int64_str_to_hex


class GearsProcessor(UnifiedProcessor):
    def proto_template(self):
        return Gears()

    def process_proto(self, gears):
        gears_output = []
        for gear in gears.gears:
            gears_output.append(
                {
                    "id": id_int64_to_hex(gear.identity.id),
                    "name": gear.identity.name.lower(),
                    "name_placeholder": gear.info.name_placeholder,
                    "image": gear.info.image,
                    "priority": gear.info.sort_priority,
                    "slot_name": gear.info.gear_slot_identity.name,
                    "level": gear.info.level,
                }
            )
        return gears_output

    def process_json(self, obj):
        gears = []
        for raw_gear in obj["Objects"].values():
            if "EquipmentSlot" not in raw_gear:
                continue
            gears.append(
                {
                    "id": id_int64_str_to_hex(raw_gear["DID"]["ID"]),
                    "name": raw_gear["DID"]["Name"].lower(),
                    "name_placeholder": raw_gear["Name"],
                    "image": raw_gear["Sprite"],
                    "priority": raw_gear["SortPriority"],
                    "slot_name": raw_gear["EquipmentSlot"]["Name"],
                    "level": raw_gear["RequiredLordLevel"],
                }
            )
        return gears

    def description(self):
        return "Gears (event and non event)"

    def key_names(self):
        return ["id", "name"]
