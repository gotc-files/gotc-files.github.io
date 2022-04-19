from files.proto_processor import ProtoProcessor
from files.util import id_int64_str_to_hex
from files.armory_collections.armory_collections_pb2 import ArmoryCollections


class ArmoryCollectionsProcessor(ProtoProcessor):
    def proto_template(self):
        return ArmoryCollections()

    def process_proto(self, armory_collections):
        armory_collections_output = []
        for armory_collection in armory_collections.armory_collections:
            armory_collections_output.append({
                "id": id_int64_str_to_hex(armory_collection.identity.id),
                "name": armory_collection.identity.name,
                "name_placeholder": armory_collection.info.name_placeholder,
                "gear_set_name": armory_collection.info.gear_set.name,
                "priority": armory_collection.info.priority,
                "bonuses": [bonus.bonus_info.name for bonus in armory_collection.info.bonuses]
            })
        return sorted(armory_collections_output, key=lambda g: g["priority"])

    def description(self):
        return 'Armory collection information'

    def key_name(self):
        return 'gear_set_name'
