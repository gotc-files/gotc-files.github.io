from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException

VALID_EQUIPMENT_SLOTS = ["helmet", "chest", "pants", "weapon", "ring", "boots"]


class TemplateProcessor(PageProcessor):
    def process(self):
        self.material_map = {}
        recipes = self._process_recipes()
        materials = self._process_materials()
        return {
            "recipes": recipes,
            "materials": materials,
        }

    def _process_recipes(self):
        recipes = []
        for raw_recipe in self.iterate_file("crafting_recipes_1"):
            if not any(
                [
                    raw_recipe["name"].startswith("eq_standard_%s" % slot)
                    for slot in VALID_EQUIPMENT_SLOTS
                ]
            ):
                continue
            recipes.append(self._process_recipe(raw_recipe))
        return recipes

    def _process_recipe(self, raw_recipe):
        gear = self.lookup_file("gears_1", "name", raw_recipe["name"])
        if not gear:
            raise InsufficientDataException("Gear %s not found" % raw_recipe["name"])
        return {
            "id": raw_recipe["id"],
            "name": self.translate(gear["name_placeholder"]),
            "steel_cost": raw_recipe["steel_cost"],
            "upgrade_time_seconds": raw_recipe["upgrade_time_seconds"],
            "level": gear["level"],
            "ingredients": [
                {
                    "id": self._process_material(ingredient["item_name"]),
                    "quantity": ingredient["quantity"],
                }
                for ingredient in raw_recipe["ingredients"]
            ],
        }

    def _process_materials(self):
        return list(
            map(
                lambda material: {
                    "id": material["id"],
                    "name": material["name"],
                },
                sorted(
                    self.material_map.values(),
                    key=lambda material: material["priority"],
                ),
            )
        )

    def _process_material(self, material_name):
        if material_name in self.material_map:
            return self.material_map[material_name]["id"]
        material = self.lookup_file("items", "name", material_name)
        if not material:
            raise InsufficientDataException("Material %s not found" % material_name)
        self.material_map[material_name] = {
            "id": material["id"],
            "name": self.translate(material["name_placeholder"]),
            "priority": material["priority"],
        }
        return self.material_map[material_name]["id"]
