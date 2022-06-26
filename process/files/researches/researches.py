from files.unified_processor import UnifiedProcessor
from files.researches.researches_pb2 import Researches
from files.util import id_int64_to_hex, id_int64_str_to_hex


class ResearchesProcessor(UnifiedProcessor):
    def proto_template(self):
        return Researches()

    def process_proto(self, researches):
        researches_output = []

        for research in researches.researches:
            info = research.info
            research_output = {
                "id": id_int64_to_hex(research.identity.id),
                "name": research.identity.name,
                "name_placeholder": info.name_placeholder,
                "description_placeholder": info.description_placeholder,
                "category": info.category.name,
                "num_levels": info.num_levels,
                "time_progression": info.time_progression.name,
                "power_progression": info.power_progression.name,
                "building_level_progression": info.building_level_progression.name,
                "requirements": [
                    {"research": requirement.research.name, "level": requirement.level}
                    for requirement in info.requirements
                ],
                "event_score_progression": info.event_score_progression.name,
                "costs": [
                    {"item_name": cost.item.name, "progression": cost.progression.name}
                    for cost in info.costs
                ],
            }
            if len(info.dragon_requirements) == 2:
                research_output[
                    "dragon_pit_requirement_progression"
                ] = info.dragon_requirements[0].progression.name
                research_output[
                    "dragon_requirement_progression"
                ] = info.dragon_requirements[1].progression.name
            researches_output.append(research_output)
        return researches_output

    def process_json(self, obj):
        researches = []
        for raw_research in obj["Objects"].values():
            researches.append(
                {
                    "id": id_int64_str_to_hex(raw_research["DID"]["ID"]),
                    "name": raw_research["DID"]["Name"],
                    "name_placeholder": raw_research["Name"],
                    "description_placeholder": raw_research["Description"],
                    "category": raw_research["Category"]["Name"],
                    "num_levels": raw_research["MaxRanks"],
                    "time_progression": raw_research["TimeProgressionDID"]["Name"],
                    "power_progression": raw_research["PowerProgressionDID"]["Name"]
                    if "PowerProgressionDID" in raw_research
                    else "",
                    "building_level_progression": raw_research[
                        "BuildingLevelReqProgressionDID"
                    ]["Name"],
                    "event_score_progression": raw_research["EventScoreProgression"][
                        "Name"
                    ],
                    "requirements": [
                        {
                            "research": requirement["DID"]["Name"],
                            "level": requirement["Level"],
                        }
                        for requirement in raw_research["RequiredResearch"]
                    ],
                    "costs": [
                        {
                            "item_name": cost["Item"]["Name"],
                            "progression": cost["Progression"]["Name"],
                        }
                        for cost in raw_research["Costs"]
                    ],
                }
            )
        return researches

    def description(self):
        return "Researches basic information"

    def key_names(self):
        return ["name"]
