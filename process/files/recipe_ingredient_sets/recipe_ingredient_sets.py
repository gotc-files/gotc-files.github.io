from files.unified_processor import UnifiedProcessor
from files.recipe_ingredient_sets.recipe_ingredient_sets_pb2 import RecipeIngredientSets
from files.util import id_int64_to_hex, id_int64_str_to_hex


class RecipeIngredientSetsProcessor(UnifiedProcessor):
    def proto_template(self):
        return RecipeIngredientSets()

    def process_proto(self, recipe_ingredient_sets):
        recipe_ingredient_sets_output = []

        for recipe_ingredient_set in recipe_ingredient_sets.recipe_ingredient_sets:
            ingredients = recipe_ingredient_set.info.ingredients.ingredients
            recipe_ingredient_sets_output.append(
                {
                    "id": id_int64_to_hex(recipe_ingredient_set.identity.id),
                    "name": recipe_ingredient_set.identity.name,
                    "ingredients": [
                        {
                            "id": id_int64_to_hex(ingredient.identity.id),
                            "name": ingredient.identity.name,
                            "type": ingredient.type,
                            "quantity": ingredient.quantity,
                        }
                        for ingredient in ingredients
                    ],
                }
            )
        return recipe_ingredient_sets_output

    def process_json(self, obj):
        recipe_ingredient_sets = []
        for raw_ingredient_sets in obj["Objects"].values():
            recipe_ingredient_sets.append(
                {
                    "id": id_int64_str_to_hex(raw_ingredient_sets["DID"]["ID"]),
                    "name": raw_ingredient_sets["DID"]["Name"],
                    "ingredients": [
                        {
                            "id": id_int64_str_to_hex(ingredient["DID"]["ID"]),
                            "name": ingredient["DID"]["Name"],
                            "type": ingredient["bag"],
                            "quantity": int(ingredient["quantity_value"]),
                        }
                        for ingredient in raw_ingredient_sets["inputs"]["items"]
                    ],
                }
            )
        return recipe_ingredient_sets

    def description(self):
        return "Recipe ingredients"

    def key_names(self):
        return ["name"]
