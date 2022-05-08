from files.proto_processor import ProtoProcessor
from files.research_categories.research_categories_pb2 import ResearchCategories
from files.util import id_int64_to_hex


class ResearchCategoriesProcessor(ProtoProcessor):
    def proto_template(self):
        return ResearchCategories()

    def process_proto(self, research_categories):
        research_categories_output = []

        for research_category in research_categories.research_categories:
            info = research_category.info
            research_categories_output.append({
                "id": id_int64_to_hex(research_category.identity.id),
                "name": research_category.identity.name,
                "name_placeholder": info.name_placeholder,
                "description_placeholder": info.description_placeholder,
            })
        return research_categories_output

    def description(self):
        return 'Research and expedition categories'

    def key_names(self):
        return ['name']
