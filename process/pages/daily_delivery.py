import re

from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException
from files.util import hash_to_hex


def parse_pack_name(name):
    matches = re.findall(r"(.+)_[t|T]ier[0-9]+", name)
    return matches[0] if matches else name


class DailyDeliveryProcessor(PageProcessor):

    def process(self):
        packs_by_name = {}
        pack_names = []
        for raw_pack in self.iterate_files(['recurring_rewards']):
            if "annu_test" in raw_pack["name"]:
                continue
            pack_name = parse_pack_name(raw_pack["name"])
            if pack_name not in packs_by_name:
                packs_by_name[pack_name] = {
                    "packs": [],
                    "id": hash_to_hex(pack_name),
                    "name": self.translate(raw_pack["name_placeholder"])
                }
                pack_names.append(pack_name)
            try:
                packs_by_name[pack_name]["packs"].append(
                    self._process_pack(raw_pack))
            except InsufficientDataException as e:
                print(e)
                continue
        return [packs_by_name[pack_name] for pack_name in pack_names[::-1]]

    def _process_pack(self, raw_pack):
        pack = {
            "id": raw_pack["id"],
            "tier": raw_pack["tier"],
            "items": [],
            "summary": [],
        }
        for item in raw_pack["items"]:
            try:
                pack["items"].append(self._process_item(item))
            except InsufficientDataException as e:
                print(e)
                continue
        for item in raw_pack["summary"]:
            try:
                pack["summary"].append(self._process_item(item))
            except InsufficientDataException as e:
                print(e)
                continue
        return pack

    def _process_item(self, raw_item):
        item = self.lookup_files(
            ["items", "dragon_items", "gears_1", "hero_items", "items_gift", "items_event"], 'id', raw_item["id"])
        if not item:
            raise InsufficientDataException(
                "Cannot find item with id: %s" % raw_item["id"])
        return {
            "name": self.translate(item["name_placeholder"]),
            "description": self.translate(item["description_placeholder"]) if "description_placeholder" in item else None,
            "quantity": raw_item["quantity"],
        }
