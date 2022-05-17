from files.proto_processor import ProtoProcessor
from files.recipes.recipies_pb2 import Recipes
from files.util import id_int64_to_hex


class RecipesProcessor(ProtoProcessor):
    def proto_template(self):
        return Recipes()

    def process_proto(self, recipes):
        recipes_output = []

        for recipe in recipes.recipes:
            recipes_output.append({
                "id": id_int64_to_hex(recipe.identity.id),
                "name": recipe.identity.name,
                "name_placeholder": recipe.info.name_placeholder,
                "description_placeholder": recipe.info.description_placeholder,
                "display_group_name": recipe.info.display_group.name,
                "ingredients_name": recipe.info.ingredients.name,
                "priority": recipe.info.sort_priority,
                "target_quality": recipe.info.target_quality,
                "target_quantity": recipe.info.target_quantity,
                "limit": recipe.info.limit,
                "event_points": recipe.info.event_points,
                "event_name": recipe.info.event_name,

            })
        return recipes_output

    def description(self):
        return 'Recipes'
