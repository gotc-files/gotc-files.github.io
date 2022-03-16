class InsufficientDataException(Exception):
    pass


class PageProcessor:
    def __init__(self, file_data_dict):
        self.file_data_dict = file_data_dict

    def translate(self, key):
        translation = self.lookup_file('translations', key)
        if not translation:
            raise InsufficientDataException(
                'Failed to find translation for key: %s' % key)
        return translation

    def lookup_file(self, file_id, key):
        return self.lookup_files([file_id], key)

    def lookup_files(self, file_ids, key):
        for file_id in file_ids:
            if file_id not in self.file_data_dict:
                raise KeyError('File id %s invalid')
            if key in self.file_data_dict[file_id]:
                return self.file_data_dict[file_id][key]
        return None

    def iterate_files(self, file_ids):
        for file_id in file_ids:
            yield from self.iterate_file(file_id)

    def iterate_file(self, file_id):
        if file_id not in self.file_data_dict:
            raise KeyError('File id %s invalid')
        for value in self.file_data_dict[file_id]:
            yield value
