import re

from files.json_processor import JsonProcessor
from files.util import id_int64_str_to_hex


def extract_info_from_name(name):
    standard_matches = re.findall(
        r"summon_standard_(Combo[A|B])_BasicRSSOaths", name)
    if standard_matches:
        return {
            "heroes": standard_matches[0],
            "time_str": "standard",
        }
    time_matches = re.findall(
        r"summon_[a-zA-Z]+_([a-zA-Z]+)([A-Z]{3}[0-9]{2})_(Gold|Hero)", name)
    if time_matches:
        return {
            "heroes": time_matches[0][0],
            "time_str": time_matches[0][1]
        }
    legacy_grouping_matches = re.findall(
        r"summon_[a-zA-Z]+_([a-zA-Z]+)_([a-zA-Z]+)", name)
    if legacy_grouping_matches:
        return {
            "heroes": '%s (%s)' % (legacy_grouping_matches[0][0], legacy_grouping_matches[0][1]),
            "time_str": "legacy_groups",
        }
    return None


class SummonsProcessor(JsonProcessor):
    def process_json(self, obj):
        summons = []
        for summon_obj in obj["Objects"].values():
            summon = {
                "id": id_int64_str_to_hex(summon_obj["DID"]["ID"]),
                "name": summon_obj["DID"]["Name"],
                "name_placeholder": summon_obj["Name"],
                "description_placeholder": summon_obj["Description"],
                "category": summon_obj["Category"]["Name"][16:],
                "purchase_options": [option["Name"] for option in summon_obj["PurchaseOptions"]]
            }
            info = extract_info_from_name(summon_obj["DID"]["Name"])
            if info:
                summon.update(info)
            summons.append(summon)
        return summons

    def description(self):
        return 'Basic information about summon configurations'
