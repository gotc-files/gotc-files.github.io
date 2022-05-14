from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class HeroTraitsProcessor(JsonProcessor):
    def process_json(self, obj):
        hero_traits = []
        for hero_trait_obj in obj["Objects"].values():
            hero_traits.append({
                "id": id_int64_str_to_hex(hero_trait_obj["DID"]["ID"]),
                "name": hero_trait_obj["DID"]["Name"],
                "name_placeholder": hero_trait_obj["Name"],
                "description_placeholder": hero_trait_obj["Description"],
            })
        return hero_traits

    def description(self):
        return 'Hero traits information'

    def key_names(self):
        return ['name']
