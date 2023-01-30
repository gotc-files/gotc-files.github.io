class InsufficientDataException(Exception):
    pass


class PageProcessor:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def translate(self, key):
        translation = self.lookup_files(
            ["translations", "translations_delta"], "name", key
        )
        return translation if translation else "n:%s" % key

    def try_translate(self, key):
        return self.lookup_files(["translations", "translations_delta"], "name", key)

    def lookup_file(self, file_id, key_name, key):
        return self.lookup_files([file_id], key_name, key)

    def lookup_files(self, file_ids, key_name, key):
        for file_id in file_ids:
            value = self.data_manager.lookup(file_id, key_name, key)
            if value is not None:
                return value
        return None

    def iterate_files(self, file_ids):
        for file_id in file_ids:
            yield from self.iterate_file(file_id)

    def iterate_file(self, file_id):
        for value in self.data_manager.get_file_data(file_id):
            yield value
