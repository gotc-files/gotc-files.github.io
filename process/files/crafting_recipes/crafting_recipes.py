from files.unified_processor import UnifiedProcessor
from files.crafting_recipes.crafting_recipes_pb2 import CraftingRecipes
from files.util import id_int64_to_hex, id_int64_str_to_hex


class CraftingRecipesProcessor(UnifiedProcessor):
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

    def process_json(self, obj):
        recipes = []
        for raw_recipe in obj["Objects"].values():
            recipes.append(
                {
                    "id": id_int64_str_to_hex(raw_recipe["DID"]["ID"]),
                    "name": raw_recipe["DID"]["Name"],
                    "steel_cost": int(raw_recipe["SteelCost"]),
                    "upgrade_time_seconds": int(raw_recipe["Time"]),
                    "template_level": int(raw_recipe.get("RequiredEquipmentLevel", 0)),
                    "ingredients": [
                        {
                            "item_name": ingredient["Item"]["Name"],
                            "quantity": int(ingredient["Quantity"]),
                        }
                        for ingredient in raw_recipe["Materials"]
                    ],
                }
            )
        return recipes

    def description(self):
        return "Crafting recipes"

    def key_names(self):
        return ["name"]
