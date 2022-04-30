from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException


class BuildingProcessor(PageProcessor):
    def process(self):
        buildings = []
        for raw_building in self.iterate_files(["buildings"]):
            if raw_building["enhancement_related_building"]:
                continue
            try:
                buildings.append(self._process_building(raw_building))
            except InsufficientDataException as e:
                print(e)
                continue
        return buildings

    def _process_building(self, raw_building):
        building_stats = self.lookup_file(
            "building_stat_sets", "name", raw_building["name"].lower())
        power_progression = self.lookup_file(
            "building_progressions", "name", raw_building["power_progression"])["values"]
        num_buildings_progression = self.lookup_file(
            "building_progressions", "name",
            raw_building["num_buildings_progression"])["values"] if raw_building["num_buildings_progression"] else None
        event_score_progression = self.lookup_file(
            "event_scoring_progressions", "name", raw_building["event_score_progression"])["values"]
        cost_progressions = [(cost_entry["item_name"], self.lookup_file(
            "building_progressions", "name", cost_entry["progression"])["values"]) for cost_entry in raw_building["costs"]]
        upgrade_time_progression = self.lookup_file(
            "building_progressions", "name", raw_building["upgrade_time_progression"])["values"]

        requirement_set_progressions = raw_building["requirement_sets"]
        return {
            "id": raw_building["id"],
            "name": self.translate(raw_building["name_placeholder"]),
            "description": self.translate(raw_building["description_placeholder"]),
            "enchancements": raw_building["building_related_enhancements"],
            "stats": [self._process_building_stat(stat["name"], stat["progression"]) for stat in building_stats["stats"]] if building_stats else [],
            "levels": [self._process_building_level(
                i,
                power_progression[i],
                num_buildings_progression[i] if num_buildings_progression else None,
                event_score_progression[i],
                [self._process_item_cost(item_name, cost_values[i])
                    for item_name, cost_values in cost_progressions],
                upgrade_time_progression[i],
                [requirement_set[i]
                    for requirement_set in requirement_set_progressions]
            ) for i in range(len(event_score_progression))]
        }

    def _process_building_level(self, index, power, num_buildings, event_score, costs, upgrade_time, requirements):
        return {
            "level": index + 1,
            "power": power,
            "num_buildings": num_buildings,
            "event_score": event_score,
            "costs": costs,
            "upgrade_time_seconds": upgrade_time,
            "requirements": [{
                "building": self.translate(self.lookup_file("buildings", "name", requirement["building"])["name_placeholder"]),
                "level": requirement["level"]
            } for requirement in requirements]
        }

    def _process_building_stat(self, stat_name, stat_progression_name):
        stat_progression = self.lookup_files(
            ["building_progressions", "generation_progressions"], "name", stat_progression_name)
        return {
            "name": self.translate(self.lookup_file("properties", "name", stat_name)["name_placeholder"]),
            "description": self.translate(self.lookup_file("properties", "name", stat_name)["description_placeholder"]),
            "progression": stat_progression["values"]
        }

    def _process_item_cost(self, item_name, cost):
        item = self.lookup_file("items", "name", item_name)
        return {
            "name": self.translate(item["name_placeholder"]),
            "description": self.translate(item["description_placeholder"]),
            "cost": cost,
        }
