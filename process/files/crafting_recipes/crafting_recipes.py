from files.proto_processor import ProtoProcessor
from files.crafting_recipes.crafting_recipes_pb2 import CraftingRecipes
from files.util import id_int64_to_hex


class CraftingRecipesProcessor(ProtoProcessor):
    def proto_template(self):
        return CraftingRecipes()

    def process_proto(self, recipes):
        recipes_output = []

        for recipe in recipes.recipes:
            recipes_output.append(
                {
                    "id": id_int64_to_hex(recipe.identity.id),
                    "name": recipe.identity.name,
                    "ingredients": [
                        {
                            "item_name": ingredient.material.name,
                            "quantity": ingredient.quantity,
                        }
                        for ingredient in recipe.info.ingredients
                    ],
                    "steel_cost": recipe.info.steel_cost,
                    "upgrade_time_seconds": recipe.info.upgrade_time_seconds,
                    "template_level": recipe.info.template_level,
                }
            )
        return recipes_output

    def description(self):
        return "Crafting recipes"

    def key_names(self):
        return ["name"]
