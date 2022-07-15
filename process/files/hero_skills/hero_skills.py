from files.hero_skills.hero_skills_pb2 import HeroSkills
from files.unified_processor import UnifiedProcessor
from files.util import id_int64_to_hex, id_int64_str_to_hex


class HeroSkillsProcessor(UnifiedProcessor):
    def proto_template(self):
        return HeroSkills()

    def process_proto(self, hero_skills):
        hero_skills_output = []
        for hero_skill in hero_skills.hero_skills:
            value = hero_skill.info.values[0]
            hero_skill_output = {
                "id": id_int64_to_hex(hero_skill.identity.id),
                "name": hero_skill.identity.name,
                "skill_type": hero_skill.info.skill_type,
                "unlock_level": hero_skill.info.unlock_level,
                "stat_name": value.stat.name,
            }
            if value.star_skill_value:
                hero_skill_output["star_skill_value"] = value.star_skill_value
            if value.progression.name:
                hero_skill_output[
                    "signature_skill_progression_name"
                ] = value.progression.name
            hero_skills_output.append(hero_skill_output)
        return hero_skills_output

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
