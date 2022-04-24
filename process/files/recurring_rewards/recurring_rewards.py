from files.proto_processor import ProtoProcessor
from files.recurring_rewards.recurring_rewards_pb2 import RecurringRewardsLists
from files.util import id_int64_to_hex


class RecurringRewardsProcessor(ProtoProcessor):

    def proto_template(self):
        return RecurringRewardsLists()

    def process_proto(self, recurring_rewards_lists):
        recurring_rewards_output = []
        for raw_recurring_rewards_list in recurring_rewards_lists.recurring_rewards_lists:
            recurring_rewards_output.append({
                "id": id_int64_to_hex(raw_recurring_rewards_list.identity.id),
                "name": raw_recurring_rewards_list.identity.name,
                "name_placeholder": raw_recurring_rewards_list.info.name_placeholder,
                "tier": raw_recurring_rewards_list.info.tier,
                "collection_interval_seconds": raw_recurring_rewards_list.info.collection_interval_seconds,
                "num_collections": raw_recurring_rewards_list.info.num_collections,
                "items": [self._process_item_legacy(item) for item in raw_recurring_rewards_list.info.items_legacy]
                if raw_recurring_rewards_list.info.items_type == 1
                else [self._process_item(item) for item in raw_recurring_rewards_list.info.items],
                "summary": [self._process_item(item) for item in raw_recurring_rewards_list.info.items_summary],
            })
        return recurring_rewards_output

    def _process_item_legacy(self, item):
        return {
            "id": id_int64_to_hex(item.id),
            "quantity": item.quantity,
        }

    def _process_item(self, item):
        return {
            "id": id_int64_to_hex(item.identity.id),
            "quantity": item.quantity,
        }

    def description(self):
        return 'Recurring rewards (including daily delivery packs) info'
