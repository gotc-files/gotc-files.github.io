from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class HeroTraitsProcessor(JsonProcessor):
    def process_json(self, obj):
        hero_traits = []
        for raw_trait in obj["Objects"].values():
            hero_traits.append(
                {
                    "id": id_int64_str_to_hex(raw_trait["DID"]["ID"]),
                    "name": raw_trait["DID"]["Name"],
                    "name_placeholder": raw_trait["Name"],
                    "description_placeholder": raw_trait["Description"],
                }
            )
        return hero_traits

    def description(self):
        return "Hero traits information"

    def key_names(self):
        return ["name"]
