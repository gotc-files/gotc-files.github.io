from files.proto_processor import ProtoProcessor
from files.armory_stat_sets.armory_stat_sets_pb2 import ArmoryStatSets
from files.util import id_int64_to_hex


class ArmoryStatSetsProcessor(ProtoProcessor):

    def proto_template(self):
        return ArmoryStatSets()

    def process_proto(self, armory_stat_sets):
        armory_stat_sets_output = []

        for armory_stat_set in armory_stat_sets.armory_stat_sets:
            armory_stat_sets_output.append({
                "id": id_int64_to_hex(armory_stat_set.armory_stat_identity.id),
                "name": armory_stat_set.armory_stat_identity.name,
                "property": armory_stat_set.wrapper.info.property.name,
                "progression": armory_stat_set.wrapper.info.progression.name,
            })
        return armory_stat_sets_output

    def description(self):
        return 'Armory stat for each collection'

    def key_names(self):
        return ['name']
