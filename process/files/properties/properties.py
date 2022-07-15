from files.unified_processor import UnifiedProcessor
from files.properties.properties_pb2 import Properties
from files.util import id_int64_to_hex, id_int64_str_to_hex


class PropertiesProcessor(UnifiedProcessor):
    def proto_template(self):
        return Properties()

    def process_proto(self, properties):
        properties_output = []

        for property in properties.properties:
            properties_output.append(
                {
                    "id": id_int64_to_hex(property.identity.id),
                    "name": property.identity.name,
                    "name_placeholder": property.info.name_placeholder,
                    "description_placeholder": property.info.description_placeholder,
                    "image": property.info.image,
                    "type": property.info.type,
                }
            )
        return properties_output

    def process_json(self, obj):
        properties = []
        for raw_property in obj["Objects"].values():
            properties.append(
                {
                    "id": id_int64_str_to_hex(raw_property["DID"]["ID"]),
                    "name": raw_property["DID"]["Name"],
                    "name_placeholder": raw_property.get("Name", ""),
                    "description_placeholder": raw_property.get("Description", ""),
                    "image": raw_property.get("Icon", ""),
                    "type": raw_property["BuffSource"],
                }
            )
        return properties

    def description(self):
        return "Properties like stats"

    def key_names(self):
        return ["name"]
