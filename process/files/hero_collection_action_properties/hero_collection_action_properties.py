from files.proto_processor import ProtoProcessor
from files.hero_collection_action_properties.hero_collection_action_properties_pb2 import HeroCollectionActionProperties
from files.util import id_int64_to_hex


class HeroCollectionActionPropertiesProcessor(ProtoProcessor):

    def proto_template(self):
        return HeroCollectionActionProperties()

    def process_proto(self, hero_collection_action_properties):
        properties_output = []

        for property in hero_collection_action_properties.properties:
            info = property.info
            if len(info.integer_property.values) > 0:
                properties_output.append({
                    "id": id_int64_to_hex(info.integer_property.identity.id),
                    "name": info.integer_property.identity.name,
                    "values": list(info.integer_property.values)
                })
            elif len(info.double_property.values) > 0:
                properties_output.append({
                    "id": id_int64_to_hex(info.double_property.identity.id),
                    "name": info.double_property.identity.name,
                    "values": list(info.double_property.values)
                })
        return properties_output

    def description(self):
        return 'Hero Collection Actions property progressions'

    def key_name(self):
        return 'name'
