from files.proto_processor import ProtoProcessor
from files.armory_stat_progressions.armory_stat_progressions_pb2 import ArmoryStatProgressions
from files.util import id_int64_to_hex


class ArmoryStatProgressionsProcessor(ProtoProcessor):

    def proto_template(self):
        return ArmoryStatProgressions()

    def process_proto(self, armory_stat_progressions):
        armory_stat_progressions_output = []

        for armory_stat_progression in armory_stat_progressions.armory_stat_progressions:
            info = armory_stat_progression.info
            if len(info.int_stats.stats) > 0:
                armory_stat_progressions_output.append({
                    "id": id_int64_to_hex(info.int_stats.identity.id),
                    "name": info.int_stats.identity.name,
                    "stats": list(info.int_stats.stats)
                })
            elif len(info.double_stats.stats) > 0:
                armory_stat_progressions_output.append({
                    "id": id_int64_to_hex(info.double_stats.identity.id),
                    "name": info.double_stats.identity.name,
                    "stats": list(info.double_stats.stats)
                })
        return armory_stat_progressions_output

    def description(self):
        return 'Armory stat names to their values'

    def key_name(self):
        return 'name'
