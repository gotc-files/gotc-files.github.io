from files.proto_processor import ProtoProcessor
from files.items.items_pb2 import Items
from files.util import id_int64_to_hex


class ItemsProcessor(ProtoProcessor):
    def proto_template(self):
        return Items()

    def process_proto(self, items):
        items_output = []

        for item in items.items:
            items_output.append({
                "id": id_int64_to_hex(item.identity.id),
                "name": item.identity.name,
                "name_placeholder": item.info.name_placeholder,
                "description_placeholder": item.info.description_placeholder,
                "image": item.info.image,
                "priority": item.info.sort_priority,
                "type": item.info.item_type.name,
            })
        return items_output

    def description(self):
        return 'Items'

    def key_names(self):
        return ['id', 'name']
