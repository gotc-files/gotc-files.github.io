from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class ItemsProcessor(JsonProcessor):
    def process_json(self, obj):
        items = []
        for raw_item in obj["Objects"].values():
            items.append(
                {
                    "id": id_int64_str_to_hex(raw_item["DID"]["ID"]),
                    "name": raw_item["DID"]["Name"],
                    "name_placeholder": raw_item.get("Name", ""),
                    "description_placeholder": raw_item.get("Description", ""),
                    "image": raw_item.get("Sprite", ""),
                    "priority": raw_item.get("SortPriority", 0),
                    "type": raw_item["DefaultBag"]["Name"]
                    if "DefaultBag" in raw_item
                    else "",
                }
            )
        return items

    def description(self):
        return "Items"

    def key_names(self):
        return ["id", "name"]
