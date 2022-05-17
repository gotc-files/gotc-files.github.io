from files.proto_processor import ProtoProcessor
from files.troops.troops_pb2 import Troops
from files.util import id_int64_to_hex


class TroopsProcessor(ProtoProcessor):
    def proto_template(self):
        return Troops()

    def process_proto(self, troops):
        troops_output = []

        for troop in troops.troops:
            troops_output.append(
                {
                    "id": id_int64_to_hex(troop.identity.id),
                    "name": troop.identity.name,
                    "name_placeholder": troop.info.name_placeholder,
                    "description_placeholder": troop.info.description_placeholder,
                }
            )
        return troops_output

    def description(self):
        return "Basic information about troops"

    def key_names(self):
        return ["id"]
