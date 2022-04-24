from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class HeroSkillsProcessor(JsonProcessor):
    def process_json(self, obj):
        hero_skills = []
        for hero_skill_obj in obj["Objects"].values():
            modifier = hero_skill_obj["PropertyModifiers"][0]
            hero_skill = {
                "id": id_int64_str_to_hex(hero_skill_obj["DID"]["ID"]),
                "name": hero_skill_obj["DID"]["Name"],
                "skill_type": hero_skill_obj["SkillType"],
                "unlock_level": hero_skill_obj.get("UnlockLevel", 0),
                "stat_name": modifier["TargetProperty"]["Name"],
            }
            if "Modifier" in modifier:
                hero_skill["star_skill_value"] = modifier["Modifier"]
            if "ModifierProgression" in modifier:
                hero_skill["signature_skill_progression_name"] = modifier["ModifierProgression"]["Name"]
            hero_skills.append(hero_skill)
        return hero_skills

    def description(self):
        return 'Hero skill definitions'

    def key_names(self):
        return ['name']
