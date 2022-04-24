from collections import OrderedDict

from files.proto_processor import ProtoProcessor
from files.summon_odds.summon_odds_pb2 import SummonOddsLists
from files.util import id_int64_to_hex


class SummonOddsProcessor(ProtoProcessor):
    def proto_template(self):
        return SummonOddsLists()

    def process_proto(self, summon_odds_lists):
        summon_odds_by_option = OrderedDict()

        for summon_odds_list in summon_odds_lists.summon_odds_lists:
            purchase_option = summon_odds_list.info.purchase_option
            if purchase_option.id not in summon_odds_by_option:
                summon_odds_by_option[purchase_option.id] = {
                    "id": id_int64_to_hex(purchase_option.id),
                    "name": purchase_option.name,
                    "odds": []
                }
            summon_odds_by_option[purchase_option.id]["odds"].append({
                "name": summon_odds_list.id.name,
                "item_id": id_int64_to_hex(summon_odds_list.info.item.id),
                "item_name": summon_odds_list.info.item.name,
                "quantity": summon_odds_list.info.quantity,
                "probability": summon_odds_list.info.probability,
            })
        return list(summon_odds_by_option.values())

    def description(self):
        return 'Summon odds by purchase option'

    def key_names(self):
        return ['name']
