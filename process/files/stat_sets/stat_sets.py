from files.unified_processor import UnifiedProcessor
from files.stat_sets.stat_sets_pb2 import StatSets
from files.util import id_int64_to_hex


class StatSetsProcessor(UnifiedProcessor):
    def proto_template(self):
        return StatSets()

    def process_proto(self, stat_sets):
        stat_sets_output = []
        for stat_set in stat_sets.stat_sets:
            stat_sets_output.append(
                {
                    "id": id_int64_to_hex(stat_set.identity.id),
                    "name": stat_set.identity.name.lower(),
                    "stats": [
                        {
                            "name": stat.identity.name,
                            "progression": stat.progression.name,
                        }
                        for stat in stat_set.stat_list.stats
                    ],
                }
            )
        return stat_sets_output

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
