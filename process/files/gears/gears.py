from files.proto_processor import ProtoProcessor
from files.gears.gears_pb2 import Gears
from files.util import id_int64_to_hex


class GearsProcessor(ProtoProcessor):
    def proto_template(self):
        return Gears()

    def process_proto(self, gears):
        gears_output = []

        for gear in gears.gears:
            gears_output.append({
                "id": id_int64_to_hex(gear.identity.id),
                "name": gear.identity.name,
                "name_placeholder": gear.info.name_placeholder,
                "image": gear.info.image,
                "priority": gear.info.sort_priority,
                "slot_name": gear.info.slot_identity.name,
                "level": gear.info.level,
            })
        return gears_output

    def description(self):
        return 'Gears (event and non event)'

    def key_name(self):
        return 'name'
