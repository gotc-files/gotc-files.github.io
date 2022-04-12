class InsufficientDataException(Exception):
    pass


class PageProcessor:
    def __init__(self, context):
        self.file_lookup_dict = context["file_lookup_dict"]
        self.file_values_dict = context["file_values_dict"]

    def translate(self, key):
        translation = self.lookup_file('translations', key)
        return translation if translation else '%s (Not Translated)' % key

    def try_translate(self, key):
        return self.lookup_file('translations', key)

    def lookup_file(self, file_id, key):
        return self.lookup_files([file_id], key)

    def lookup_files(self, file_ids, key):
        for file_id in file_ids:
            if file_id not in self.file_lookup_dict:
                raise KeyError('File id %s invalid' & file_id)
            if key in self.file_lookup_dict[file_id]:
                return self.file_lookup_dict[file_id][key]
        return None

    def iterate_files(self, file_ids):
        for file_id in file_ids:
            yield from self.iterate_file(file_id)

    def iterate_file(self, file_id):
        if file_id not in self.file_values_dict:
            raise KeyError('File id %s invalid' % file_id)
        for value in self.file_values_dict[file_id]:
            yield value
