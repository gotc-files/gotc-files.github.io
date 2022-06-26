from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class StatSetsProcessor(JsonProcessor):
    def process_json(self, obj):
        stat_sets = []
        for raw_stat_set in obj["Objects"].values():
            stat_sets.append(
                {
                    "id": id_int64_str_to_hex(raw_stat_set["DID"]["ID"]),
                    "name": raw_stat_set["DID"]["Name"].lower(),
                    "stats": [
                        {
                            "name": stat["Property"]["Name"],
                            "progression": stat["Progression"]["Name"],
                        }
                        for stat in raw_stat_set["PropMods"]
                    ],
                }
            )
        return stat_sets

    def description(self):
        return "Sets of stats with names and progression"

    def key_names(self):
        return ["name"]
