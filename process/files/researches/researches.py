from files.proto_processor import ProtoProcessor
from files.researches.researches_pb2 import Researches
from files.util import id_int64_to_hex


class ResearchesProcessor(ProtoProcessor):
    def proto_template(self):
        return Researches()

    def process_proto(self, researches):
        researches_output = []

        for research in researches.researches:
            info = research.info
            researches_output.append({
                "id": id_int64_to_hex(research.identity.id),
                "name": research.identity.name,
                "name_placeholder": info.name_placeholder,
                "description_placeholder": info.description_placeholder,
                "category": info.category.name,
                "num_levels": info.num_levels,
                "time_progression": info.time_progression.name,
                "power_progression": info.power_progression.name,
                "building_level_progression": info.power_progression.name,
                "requirements": [{"research": requirement.research.name, "level": requirement.level}
                                 for requirement in info.requirements],
                "event_score_progression": info.event_score_progression.name,
                "costs": [{"item_name": cost.item.name, "progression": cost.progression.name} for cost in info.costs],
            })
        return researches_output

    def _process_requirement(self, requirement):
        return {"research": requirement.research.name, "level": requirement.level}

    def description(self):
        return 'Researches basic information'

    def key_names(self):
        return ['name']
