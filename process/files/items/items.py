from files.unified_processor import UnifiedProcessor
from files.items.items_pb2 import Items
from files.util import id_int64_to_hex, id_int64_str_to_hex


class ItemsProcessor(UnifiedProcessor):
    def proto_template(self):
        return Items()

    def process_proto(self, items):
        items_output = []

        for item in items.items:
            items_output.append(
                {
                    "id": id_int64_to_hex(item.identity.id),
                    "name": item.identity.name,
                    "name_placeholder": item.info.name_placeholder,
                    "description_placeholder": item.info.description_placeholder,
                    "image": item.info.image,
                    "priority": item.info.sort_priority,
                    "type": item.info.item_type.name,
                }
            )
        return items_output

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
