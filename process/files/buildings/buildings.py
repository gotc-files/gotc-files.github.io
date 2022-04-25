from files.proto_processor import ProtoProcessor
from files.buildings.buildings_pb2 import Buildings
from files.util import id_int64_to_hex


class BuildingsProcessor(ProtoProcessor):
    def proto_template(self):
        return Buildings()

    def process_proto(self, buildings):
        buildings_output = []

        for building in buildings.buildings:
            info = building.info
            buildings_output.append({
                "id": id_int64_to_hex(building.identity.id),
                "name": building.identity.name,
                "name_placeholder": info.name_placeholder,
                "description_placeholder": info.description_placeholder,
                "upgrade_time_progression": info.upgrade_time_progression.name,
                "costs": [{"item_name": cost.item.name, "progression": cost.progression.name} for cost in info.costs],
                "power_progression": info.power_progression.name,
                "requirement_sets": [self._process_requirement_set(requirement_set)
                                     for requirement_set in info.requirement_sets],
                "num_buildings_progression": info.num_buildings_progression.name,
                "stat": info.stat.name,
                "enhancement_related_building": info.enhancement_related_building.name,
                "building_related_enhancements": [enhancement.name for enhancement in info.building_related_enhancements],
            })
        return buildings_output

    def _process_requirement_set(self, requirement_set):
        return [{"building": requirement.building.name, "level": requirement.level}
                for requirement in requirement_set.requirements]

    def description(self):
        return 'Buildings and enhancements basic information'

    def key_names(self):
        return ['name']
