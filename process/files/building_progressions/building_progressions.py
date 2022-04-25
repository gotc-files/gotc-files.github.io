from files.proto_processor import ProtoProcessor
from files.building_progressions.building_progressions_pb2 import BuildingProgressions
from files.util import id_int64_to_hex


class BuildingProgressionsProcessor(ProtoProcessor):
    def proto_template(self):
        return BuildingProgressions()

    def process_proto(self, building_progressions):
        progressions_output = []

        for progression in building_progressions.building_progressions:
            info = progression.info
            if len(info.int_values.values) > 0:
                progressions_output.append({
                    "id": id_int64_to_hex(info.int_values.identity.id),
                    "name": info.int_values.identity.name,
                    "values": list(info.int_values.values)
                })
            elif len(info.double_values.values) > 0:
                progressions_output.append({
                    "id": id_int64_to_hex(info.double_values.identity.id),
                    "name": info.double_values.identity.name,
                    "values": list(info.double_values.values)
                })
        return progressions_output

    def description(self):
        return 'Building related value progressions'

    def key_names(self):
        return ['name']
