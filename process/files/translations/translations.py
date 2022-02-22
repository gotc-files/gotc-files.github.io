import json

from files.file_processor import FileProcessor


class TranslationsProcessor(FileProcessor):
    def __init__(self, file_path):
        super().__init__(file_path)

    def process_values(self):
        with open(self.file_path) as f:
            content = f.read()
            entries = content.split('¯¯')
            pairs = [entry.split('¬¬')
                     for entry in entries if len(entry.split('¬¬')) >= 2]
            return list(map(lambda pair: {"name": pair[0], "value": pair[1]}, pairs))

    def description(self):
        return 'Translations for a specific language'

    def key_name(self):
        return "name"

    def value_name(self):
        return "value"
