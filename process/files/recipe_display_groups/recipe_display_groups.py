from files.recipe_display_groups.recipe_display_groups_pb2 import RecipeDisplayGroups
from files.util import id_int64_to_hex
from files.proto_processor import ProtoProcessor


class RecipeDisplayGroupsProcessor(ProtoProcessor):
    def proto_template(self):
        return RecipeDisplayGroups()

    def process_proto(self, recipe_display_groups):
        recipe_display_groups_output = []
        for recipe_display_group in recipe_display_groups.recipe_display_groups:
            recipe_display_groups_output.append(
                {
                    "id": id_int64_to_hex(recipe_display_group.identity.id),
                    "name": recipe_display_group.identity.name,
                    "name_placeholder": recipe_display_group.info.name_placeholder,
                }
            )
        return recipe_display_groups_output

    def description(self):
        return "Recipe display groups information"

    def key_names(self):
        return ["name"]
