from files.proto_processor import ProtoProcessor
from files.gear_set_progressions.gear_set_progressions_pb2 import GearSetProgressions
from files.util import id_int64_str_to_hex


def deduplicate_with_order(values):
    value_set = set()
    deduplicated_values = []
    for value in values:
        if value not in value_set:
            value_set.add(value)
            deduplicated_values.append(value)
    return deduplicated_values


class GearSetProgressionsProcessor(ProtoProcessor):

    def proto_template(self):
        return GearSetProgressions()

    def process_proto(self, gear_set_progressions):
        gear_set_progressions_output = []
        for gear_set_progression in gear_set_progressions.gear_set_progressions:
            if not gear_set_progression.info.gear_set:
                continue
            gear_set = gear_set_progression.info.gear_set
            gear_set_progressions_output.append({
                "id": id_int64_str_to_hex(gear_set.identity.id),
                "name": gear_set.identity.name,
                "gear_names_with_level": deduplicate_with_order([name.lower() for name in gear_set.gear_names_with_level])
            })
        return gear_set_progressions_output

    def description(self):
        return 'Gear set to gear names with level'

    def key_name(self):
        return 'name'
