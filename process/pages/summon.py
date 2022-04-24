from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException


class SummonProcessor(PageProcessor):

    def process(self):
        summons = []
        for raw_summon in self.iterate_files(['summons']):
            try:
                summons.append(self._process_summon(raw_summon))
            except InsufficientDataException as e:
                print(e)
                continue
        return summons

    def _process_summon(self, raw_summon):
        return {
            "id": raw_summon["id"],
            "name": self.translate(raw_summon["name_placeholder"]),
            "description": self.translate(raw_summon["description_placeholder"]),
            "time_str": raw_summon.get("time_str", ""),
            "heroes": raw_summon.get("heroes", ""),
            "category": raw_summon["category"],
            "purchase_options": [self._process_purchase_option(purchase_option_name)
                                 for purchase_option_name in raw_summon["purchase_options"]],
        }

    def _process_purchase_option(self, purchase_option_name):
        purchase_option = self.lookup_file(
            "summon_odds", 'name', purchase_option_name)
        if not purchase_option:
            raise InsufficientDataException(
                'Cannot find summon purchase option %s' % purchase_option_name)
        return {
            "name": purchase_option_name,
            "odds": [self._process_odds(odds) for odds in purchase_option["odds"]],
        }

    def _process_odds(self, odds):
        reward = self.lookup_files(
            ["heroes", "hero_items", "items", "dragon_items"], 'name', odds["item_name"])
        if not reward:
            reward = self.lookup_file("gears_1", 'name', odds["item_name"])
        if not reward:
            raise InsufficientDataException(
                "Cannot find item or hero with id: %s" % odds["item_name"])
        return {
            "name": self.translate(reward["name_placeholder"]),
            "description": self.translate(reward["description_placeholder"]) if "description_placeholder" in reward else "",
            "quantity": odds["quantity"],
            "probability": odds["probability"],
        }
