from files.hero_traits.hero_traits_pb2 import HeroTraits
from files.unified_processor import UnifiedProcessor
from files.util import id_int64_to_hex


class HeroTraitsProcessor(UnifiedProcessor):
    def proto_template(self):
        return HeroTraits()

    def process_proto(self, hero_traits):
        hero_traits_output = []
        for hero_trait in hero_traits.hero_traits:
            hero_traits_output.append(
                {
                    "id": id_int64_to_hex(hero_trait.identity.id),
                    "name": hero_trait.identity.name,
                    "name_placeholder": hero_trait.info.name_placeholder,
                    "description_placeholder": hero_trait.info.description_placeholder,
                }
            )
        return hero_traits_output

    def description(self):
        return "Hero traits information"

    def key_names(self):
        return ["name"]
