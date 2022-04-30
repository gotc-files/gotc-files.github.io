from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class EventScoringProgressionsProcessor(JsonProcessor):
    def process_json(self, obj):
        progressions_output = []
        for progression in obj["Progressions"].values():
            progressions_output.append({
                "id": id_int64_str_to_hex(progression["DID"]["ID"]),
                "name": progression["DID"]["Name"],
                "values": [int(str_value) for str_value in progression["Entries"]],
            })
        return progressions_output

    def description(self):
        return 'Event scoring progression values'

    def key_names(self):
        return ['name']
