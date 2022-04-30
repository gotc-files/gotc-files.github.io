from files.proto_processor import ProtoProcessor
from files.stat_sets.stat_sets_pb2 import StatSets
from files.util import id_int64_to_hex


class StatSetsProcessor(ProtoProcessor):

    def proto_template(self):
        return StatSets()

    def process_proto(self, stat_sets):
        stat_sets_output = []
        for stat_set in stat_sets.stat_sets:
            stat_sets_output.append({
                "id": id_int64_to_hex(stat_set.identity.id),
                "name": stat_set.identity.name.lower(),
                "stats": [{
                    "name": stat.identity.name,
                    "progression": stat.progression.name
                } for stat in stat_set.stat_list.stats]
            })
        return stat_sets_output

    def description(self):
        return 'Sets of stats with names and progression'

    def key_names(self):
        return ['name']
