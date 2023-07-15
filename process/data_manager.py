from collections import defaultdict


class DataManager:
    def __init__(self):
        self.data = {}
        self.indexes = defaultdict(dict)

    def add_file_data(self, file_id, values, key_names, value_name):
        self.data[file_id] = values
        for key_name in key_names:
            self.indexes[file_id][key_name] = {
                value[key_name].lower(): (value[value_name] if value_name else value)
                for value in values
            }

    def lookup(self, file_id, key_name, key):
        if file_id not in self.indexes:
            return None
        file_indexes = self.indexes[file_id]
        if key_name not in file_indexes:
            return None
        return file_indexes[key_name].get(key.lower(), None)

    def get_file_data(self, file_id):
        return self.data[file_id]
