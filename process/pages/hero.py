from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException


def to_property_name(stat_name):
    if stat_name.startswith("driven_"):
        return "property_" + stat_name[7:] + "_hero"
    return stat_name


class HeroProcessor(PageProcessor):

    def process(self):
        heroes = []
        for raw_hero in self.iterate_files(['heroes']):
            try:
                heroes.append(self._process_hero(raw_hero))
            except InsufficientDataException as e:
                print(e)
                continue
        return heroes

    def _process_hero(self, raw_hero):
        hero = {
            "id": raw_hero["id"],
            "name": self.translate(raw_hero["name_placeholder"]),
            "description": self.translate(raw_hero["description_placeholder"]),
            "skills": [self._process_skill(skill_name) for skill_name in raw_hero["skills"]],
            "rarity": raw_hero["rarity"],
            "max_stars": raw_hero["max_stars"],
        }

        return hero

    def _process_skill(self, skill_name):
        raw_skill = self.lookup_file('hero_skills', skill_name)
        stat = self.lookup_file(
            'properties', to_property_name(raw_skill["stat_name"]))
        skill = {
            "name": self.translate(stat["name_placeholder"]),
            "description": self.translate(stat["description_placeholder"]),
            "type": raw_skill["skill_type"],
        }
        if "star_skill_value" in raw_skill:
            skill["star_skill_value"] = raw_skill["star_skill_value"]
            skill["unlock_level"] = raw_skill["unlock_level"]
        if "signature_skill_progression_name" in raw_skill:
            skill["signature_skill_values"] = self.lookup_file(
                'hero_skill_progressions', raw_skill["signature_skill_progression_name"])["values"]
        return skill
