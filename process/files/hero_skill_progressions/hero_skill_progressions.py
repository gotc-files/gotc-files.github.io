from files.proto_processor import ProtoProcessor
from files.hero_skill_progressions.hero_skill_progressions_pb2 import HeroSkillProgressions
from files.util import id_int64_to_hex


class HeroSkillProgressionsProcessor(ProtoProcessor):

    def proto_template(self):
        return HeroSkillProgressions()

    def process_proto(self, hero_skill_progressions):
        hero_skill_progressions_output = []

        for hero_skill_progression in hero_skill_progressions.hero_skill_progressions:
            info = hero_skill_progression.info
            if len(info.int_stats.stats) > 0:
                hero_skill_progressions_output.append({
                    "id": id_int64_to_hex(info.int_stats.identity.id),
                    "name": info.int_stats.identity.name,
                    "values": list(info.int_stats.stats)
                })
            elif len(info.double_stats.stats) > 0:
                hero_skill_progressions_output.append({
                    "id": id_int64_to_hex(info.double_stats.identity.id),
                    "name": info.double_stats.identity.name,
                    "values": list(info.double_stats.stats)
                })
        return hero_skill_progressions_output

    def description(self):
        return 'Hero skill progressions'

    def key_name(self):
        return 'name'
