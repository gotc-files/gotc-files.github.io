from files.proto_processor import ProtoProcessor
from files.gear_stat_sets.gear_stat_sets_pb2 import GearStatSets
from files.util import id_int64_to_hex


class GearStatSetsProcessor(ProtoProcessor):

    def proto_template(self):
        return GearStatSets()

    def process_proto(self, gear_stat_sets):
        gear_stat_sets_output = []

        for gear_stat_set in gear_stat_sets.gear_stat_sets:
            gear_stat_sets_output.append({
                "id": id_int64_to_hex(gear_stat_set.gear_identity.id),
                "name": gear_stat_set.gear_identity.name.lower(),
                "stats": [{
                    "name": gear_stat.identity.name,
                    "progression": gear_stat.progression.name
                } for gear_stat in gear_stat_set.gear_stat_list.gear_stats]
            })
        return gear_stat_sets_output

    def description(self):
        return 'Gear names to their stat lists'

    def key_names(self):
        return ['name']
