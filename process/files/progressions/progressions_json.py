from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class ProgressionsJsonProcessor(JsonProcessor):
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
