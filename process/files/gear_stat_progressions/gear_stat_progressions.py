from files.proto_processor import ProtoProcessor
from files.gear_stat_progressions.gear_stat_progressions_pb2 import GearStatProgressions
from files.util import id_int64_to_hex


class GearStatProgressionsProcessor(ProtoProcessor):

    def proto_template(self):
        return GearStatProgressions()

    def process_proto(self, gear_stat_progressions):
        gear_stat_progressions_output = []

        for gear_stat_progression in gear_stat_progressions.gear_stat_progressions:
            info = gear_stat_progression.info
            if len(info.int_stats.stats) > 0:
                gear_stat_progressions_output.append({
                    "id": id_int64_to_hex(info.int_stats.identity.id),
                    "name": info.int_stats.identity.name,
                    "stats": list(info.int_stats.stats)
                })
            elif len(info.double_stats.stats) > 0:
                gear_stat_progressions_output.append({
                    "id": id_int64_to_hex(info.double_stats.identity.id),
                    "name": info.double_stats.identity.name,
                    "stats": list(info.double_stats.stats)
                })
        return gear_stat_progressions_output

    def description(self):
        return 'Gear stat names to their values'

    def key_name(self):
        return 'name'
