from files.proto_processor import ProtoProcessor
from files.util import id_int64_to_hex
from files.hero_collection_actions.hero_collection_actions_pb2 import (
    HeroCollectionActions,
)


class HeroCollectionActionsProcessor(ProtoProcessor):
    def proto_template(self):
        return HeroCollectionActions()

    def process_proto(self, actions):
        actions_output = []
        for action in actions.hero_collection_actions:
            action_output = {
                "id": id_int64_to_hex(action.identity.id),
                "name": action.identity.name,
                "name_placeholder": action.info.name_placeholder,
                "description_placeholder": action.info.description_placeholder,
                "tag": "UTILITY" if action.info.is_utility else "COMBAT",
                "image": action.info.image,
                "property_name": action.info.stat.property.name,
                "buff_progression_name": action.info.stat.progression.name,
                "duration_progression_name": action.info.duration_progression.name,
                "cooldown_progression_name": action.info.cooldown_progression.name,
                "incluence_cost_progression_name": action.info.influence_progression.name,
                "level_progression_name": action.info.level_progression.name,
            }
            if action.info.num_uses_progression.name:
                action_output[
                    "num_uses_progression_name"
                ] = action.info.num_uses_progression.name
            actions_output.append(action_output)
        return actions_output

    def description(self):
        return "Basic information about all hero collection actions"
