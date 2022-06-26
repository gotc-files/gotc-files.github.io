from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class HeroSkillsProcessor(JsonProcessor):
    def process_json(self, obj):
        hero_skills = []
        for raw_skill in obj["Objects"].values():
            value = raw_skill["PropertyModifiers"][0]
            hero_skill = {
                "id": id_int64_str_to_hex(raw_skill["DID"]["ID"]),
                "name": raw_skill["DID"]["Name"],
                "skill_type": raw_skill["SkillType"],
                "unlock_level": raw_skill.get("UnlockLevel", 0),
                "stat_name": value["TargetProperty"]["Name"],
            }
            if "Modifier" in value:
                hero_skill["star_skill_value"] = value["Modifier"]
            if "ModifierProgression" in value:
                hero_skill["signature_skill_progression_name"] = value[
                    "ModifierProgression"
                ]["Name"]
            hero_skills.append(hero_skill)
        return hero_skills

    def description(self):
        return "Hero skill definitions"

    def key_names(self):
        return ["name"]
