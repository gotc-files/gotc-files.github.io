from files.util import id_int64_to_hex
from files.proto_processor import ProtoProcessor
from files.heroes.heroes_pb2 import Heroes


class HeroesProcessor(ProtoProcessor):
    def proto_template(self):
        return Heroes()

    def process_proto(self, heroes):
        heroes_output = []
        for hero in heroes.heroes:
            hero_output = {
                "id": id_int64_to_hex(hero.identity.id),
                "name": hero.identity.name,
                "name_placeholder": hero.info.name_placeholder,
                "description_placeholder": hero.info.description_placeholder,
                "rarity": hero.info.rarity,
                "max_stars": hero.info.max_stars,
                "xp_progression_name": hero.info.xp_progression.name,
                "event_score_progression_name": hero.info.event_score_progression.name,
                "skills": [skill.name for skill in hero.info.skills],
                "traits": [trait.name for trait in hero.info.traits],
            }
            for requirement in hero.info.requirements:
                if requirement.progression.name.startswith("prog_shardcost"):
                    hero_output["relic_name"] = requirement.item.name
                    hero_output["relic_progression_name"] = requirement.progression.name
                if requirement.progression.name.startswith("prog_hero_adv_stones_cost"):
                    hero_output["oath_progression_name"] = requirement.progression.name
            heroes_output.append(hero_output)
        return heroes_output

    def description(self):
        return "Basic information about all heroes"

    def key_names(self):
        return ["id", "name"]
