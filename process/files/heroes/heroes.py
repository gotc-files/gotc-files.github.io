from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class HeroesProcessor(JsonProcessor):
    def process_json(self, obj):
        heroes = []
        for hero_obj in obj["Objects"].values():
            hero = {
                "id": id_int64_str_to_hex(hero_obj["DID"]["ID"]),
                "name": hero_obj["DID"]["Name"],
                "name_placeholder": hero_obj["Name"],
                "description_placeholder": hero_obj["Description"],
                "rarity": hero_obj["Rarity"],
                "max_stars": hero_obj["MaxStars"],
                "xp_progression_name": hero_obj["XPProg"]["Name"],
                "event_score_progression_name": hero_obj["EventScoreProgression"]["Name"],
                "skills": sorted([skill["Name"] for skill in hero_obj["Skills"]]),
                "traits": [trait["Name"] for trait in hero_obj["Traits"]]
            }
            for requirement in hero_obj["LevelupReqs"]:
                if requirement["CostProg"]["Name"].startswith("prog_shardcost"):
                    hero["relic_name"] = requirement["Item"]["Name"]
                    hero["relic_progression_name"] = requirement["CostProg"]["Name"]
                if requirement["CostProg"]["Name"].startswith("prog_hero_adv_stones_cost"):
                    hero["oath_progression_name"] = requirement["CostProg"]["Name"]
            heroes.append(hero)
        return heroes

    def description(self):
        return 'Basic information about all heroes'

    def key_names(self):
        return ['id', 'name']
