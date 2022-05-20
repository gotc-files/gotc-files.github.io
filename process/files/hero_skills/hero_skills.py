from files.hero_skills.hero_skills_pb2 import HeroSkills
from files.proto_processor import ProtoProcessor
from files.util import id_int64_to_hex


class HeroSkillsProcessor(ProtoProcessor):
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

    def description(self):
        return "Hero skill definitions"

    def key_names(self):
        return ["name"]
