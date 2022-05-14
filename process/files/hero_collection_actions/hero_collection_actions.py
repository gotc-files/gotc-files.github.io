from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


class HeroCollectionActionsProcessor(JsonProcessor):
    def process_json(self, obj):
        actions_output = []
        for hca in obj["Objects"].values():
            action = {
                "id": id_int64_str_to_hex(hca["DID"]["ID"]),
                "name": hca["DID"]["Name"],
                "name_placeholder": hca["Name"],
                "description_placeholder": hca["Description"],
                "tag": hca["Tag"],
                "image": hca["Icon"],
                "property_name": hca["PropMods"][0]["Property"]["Name"],
                "buff_progression_name": hca["PropMods"][0]["Progression"]["Name"],
                "duration_progression_name": hca["DurationProg"]["Name"],
                "cooldown_progression_name": hca["CooldownProg"]["Name"],
                "incluence_cost_progression_name": hca["InfluenceCostProg"]["Name"],
                "level_progression_name": hca["LevelProg"]["Name"],
            }
            if "NumUsesProg" in hca:
                action["num_uses_progression_name"] = hca["NumUsesProg"]["Name"]
            actions_output.append(action)
        return actions_output

    def description(self):
        return 'Basic information about all hero collection actions'
