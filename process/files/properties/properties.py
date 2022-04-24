from files.proto_processor import ProtoProcessor
from files.properties.properties_pb2 import Properties
from files.util import id_int64_to_hex


class PropertiesProcessor(ProtoProcessor):
    def proto_template(self):
        return Properties()

    def process_proto(self, properties):
        properties_output = []

        for property in properties.properties:
            properties_output.append({
                "id": id_int64_to_hex(property.identity.id),
                "name": property.identity.name,
                "name_placeholder": property.info.name_placeholder,
                "description_placeholder": property.info.description_placeholder,
                "image": property.info.image,
                "type": property.info.type,
            })
        return properties_output

    def description(self):
        return 'Properties like stats'

    def key_names(self):
        return ['name']
