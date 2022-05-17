from files.proto_processor import ProtoProcessor
from files.recipe_ingredient_sets.recipe_ingredient_sets_pb2 import RecipeIngredientSets
from files.util import id_int64_to_hex


class RecipeIngredientSetsProcessor(ProtoProcessor):
    def proto_template(self):
        return RecipeIngredientSets()

    def process_proto(self, recipe_ingredient_sets):
        recipe_ingredient_sets_output = []

        for recipe_ingredient_set in recipe_ingredient_sets.recipe_ingredient_sets:
            ingredients = recipe_ingredient_set.info.ingredients.ingredients
            recipe_ingredient_sets_output.append({
                "id": id_int64_to_hex(recipe_ingredient_set.identity.id),
                "name": recipe_ingredient_set.identity.name,
                "ingredients": [{
                    "id": ingredient.identity.id,
                    "name": ingredient.identity.name,
                    "type": ingredient.type,
                    "quantity": ingredient.quantity,
                } for ingredient in ingredients]
            })
        return recipe_ingredient_sets_output

    def description(self):
        return 'Recipe ingredients'

    def key_names(self):
        return ['name']
