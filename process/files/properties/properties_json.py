from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class PropertiesProcessor(JsonProcessor):
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
