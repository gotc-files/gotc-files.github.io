from collections import OrderedDict

from files.unified_processor import UnifiedProcessor
from files.summon_odds.summon_odds_pb2 import SummonOddsLists
from files.util import id_int64_to_hex
from files.util import id_int64_str_to_hex


def group_odds_by_id(summon_odds_list):
    summon_odds_by_option = OrderedDict()
    for summon_odds in summon_odds_list:
        purchase_id = summon_odds.pop("purchase_id")
        purchase_name = summon_odds.pop("purchase_name")
        if purchase_id not in summon_odds_by_option:
            summon_odds_by_option[purchase_id] = {
                "id": purchase_id,
                "name": purchase_name,
                "odds": [],
            }
        summon_odds_by_option[purchase_id]["odds"].append(summon_odds)
    return list(summon_odds_by_option.values())


class SummonOddsProcessor(UnifiedProcessor):
    def proto_template(self):
        return SummonOddsLists()

    def process_proto(self, summon_odds_lists):
        summon_odds_lists_output = []
        for summon_odds_list in summon_odds_lists.summon_odds_lists:
            summon_odds_lists_output.append(
                {
                    "purchase_id": id_int64_to_hex(
                        summon_odds_list.info.purchase_option.id
                    ),
                    "purchase_name": summon_odds_list.info.purchase_option.name,
                    "name": summon_odds_list.id.name,
                    "item_id": id_int64_to_hex(summon_odds_list.info.item.id),
                    "item_name": summon_odds_list.info.item.name,
                    "quantity": summon_odds_list.info.quantity,
                    "probability": summon_odds_list.info.probability,
                }
            )
        return group_odds_by_id(summon_odds_lists_output)

    def process_json(self, obj):
        summon_odds_lists = []
        for raw_summon_odds_list in obj["Objects"].values():
            summon_odds_lists.append(
                {
                    "purchase_id": id_int64_str_to_hex(
                        raw_summon_odds_list["PurchaseID"]["ID"]
                    ),
                    "purchase_name": raw_summon_odds_list["PurchaseID"]["Name"],
                    "name": raw_summon_odds_list["DID"]["Name"],
                    "item_id": id_int64_str_to_hex(raw_summon_odds_list["Item"]["ID"]),
                    "item_name": raw_summon_odds_list["Item"]["Name"],
                    "quantity": int(raw_summon_odds_list["Quantity"]),
                    "probability": raw_summon_odds_list["Percent"],
                }
            )
        return group_odds_by_id(summon_odds_lists)

    def description(self):
        return "Summon odds by purchase option"

    def key_names(self):
        return ["name"]
