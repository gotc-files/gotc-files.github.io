from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException
from files.util import id_int64_to_hex

RECIPE_FILES = (
    ("monthly_trade_1", "Monthly Trade 1"),
    ("monthly_trade_2", "Monthly Trade 2"),
    ("feast_cakes", "Feast Cakes"),
    ("writs", "Writs"),
    ("repeatable", "Repeatable"),
    ("dragon", "Dragon"),
    ("flux", "Flux"),
    ("traders_script", "Traders Script"),
    ("nodes", "Nodes"),
    ("venison", "Venison"),
    ("festival", "Festival"),
    ("iron_crown", "Iron Crown"),
    ("bounties", "Bounties"),
)

INGREDIENT_FILES = (
    "dragon_items",
    "items",
    "items_event",
    "items_gift",
    "items_writs_bounties",
    "troops",
)


class RecipeProcessor(PageProcessor):
    def process(self):
        recipes = []
        for recipe_file_suffix, recipe_category in RECIPE_FILES:
            recipes_from_file = []
            for raw_recipe in self.iterate_file("recipes_%s" % recipe_file_suffix):
                try:
                    recipes_from_file.append(
                        self._process_recipe(
                            raw_recipe,
                            "recipe_ingredient_sets_%s" % recipe_file_suffix,
                            recipe_category,
                        )
                    )
                except InsufficientDataException as e:
                    print(e)
                    continue
            recipes.extend(recipes_from_file[::-1])
        return recipes

    def _process_recipe(self, raw_recipe, recipe_ingredient_sets_file, recipe_category):
        recipe_ingredients = self.lookup_file(
            recipe_ingredient_sets_file, "name", raw_recipe["ingredients_name"]
        )["ingredients"]
        return {
            "id": raw_recipe["id"],
            "name": self.translate(raw_recipe["name_placeholder"]),
            "description": self.translate(raw_recipe["description_placeholder"]),
            "category": recipe_category,
            "event_name": raw_recipe["event_name"],
            "event_points": raw_recipe["event_points"],
            "limit": raw_recipe["limit"],
            "target_quantity": raw_recipe["target_quantity"],
            "target_quality": raw_recipe["target_quality"],
            "ingredients": [
                self._process_ingredient(ingredient)
                for ingredient in recipe_ingredients
            ],
        }

    def _process_ingredient(self, ingredient):
        ingredient_id = ingredient["id"]
        ingredient_object = self.lookup_files(INGREDIENT_FILES, "id", ingredient_id)
        if ingredient_object is None:
            raise InsufficientDataException("Cannot find ingredient %s" % ingredient_id)
        return {
            "name": self.translate(ingredient_object["name_placeholder"]),
            "description": self.translate(ingredient_object["description_placeholder"]),
            "type": ingredient["type"],
            "quantity": ingredient["quantity"],
        }
