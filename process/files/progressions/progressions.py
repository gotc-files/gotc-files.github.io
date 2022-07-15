from files.unified_processor import UnifiedProcessor
from files.progressions.progressions_pb2 import Progressions
from files.util import id_int64_to_hex, id_int64_str_to_hex


class ProgressionsProcessor(UnifiedProcessor):
    def proto_template(self):
        return Progressions()

    def process_proto(self, progressions):
        progressions_output = []

        for progression in progressions.progressions:
            info = progression.info
            if len(info.int_values.values) > 0:
                progressions_output.append(
                    {
                        "id": id_int64_to_hex(info.int_values.identity.id),
                        "name": info.int_values.identity.name,
                        "values": list(info.int_values.values),
                    }
                )
            elif len(info.double_values.values) > 0:
                progressions_output.append(
                    {
                        "id": id_int64_to_hex(info.double_values.identity.id),
                        "name": info.double_values.identity.name,
                        "values": list(info.double_values.values),
                    }
                )
        return progressions_output

    def process_json(self, obj):
        progressions = []
        for raw_progression in obj["Progressions"].values():
            progressions.append(
                {
                    "id": id_int64_str_to_hex(raw_progression["DID"]["ID"]),
                    "name": raw_progression["DID"]["Name"],
                    "values": raw_progression["Entries"],
                }
            )
        return progressions

    def description(self):
        return "Progressions as a list of numeric values for each level"

    def key_names(self):
        return ["name"]
