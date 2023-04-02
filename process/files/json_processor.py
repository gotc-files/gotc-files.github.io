import json

from files.file_processor import FileProcessor


class JsonProcessor(FileProcessor):
    def __init__(self, file_path):
        super().__init__(file_path)

    def process_json(self, _):
        raise NotImplementedError()

    def process_values(self):
        return self.process_json(json.load(open(self.file_path)))
