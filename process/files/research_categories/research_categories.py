from files.unified_processor import UnifiedProcessor
from files.research_categories.research_categories_pb2 import ResearchCategories
from files.util import id_int64_to_hex, id_int64_str_to_hex


class ResearchCategoriesProcessor(UnifiedProcessor):
    def proto_template(self):
        return ResearchCategories()

    def process_proto(self, research_categories):
        research_categories_output = []

        for research_category in research_categories.research_categories:
            info = research_category.info
            research_categories_output.append(
                {
                    "id": id_int64_to_hex(research_category.identity.id),
                    "name": research_category.identity.name,
                    "name_placeholder": info.name_placeholder,
                    "description_placeholder": info.description_placeholder,
                }
            )
        return research_categories_output

    def process_json(self, obj):
        research_categories = []
        for raw_research_category in obj["Objects"].values():
            research_categories.append(
                {
                    "id": id_int64_str_to_hex(raw_research_category["DID"]["ID"]),
                    "name": raw_research_category["DID"]["Name"],
                    "name_placeholder": raw_research_category["Name"],
                    "description_placeholder": raw_research_category["Description"],
                }
            )
        return research_categories

    def description(self):
        return "Research and expedition categories"

    def key_names(self):
        return ["name"]
