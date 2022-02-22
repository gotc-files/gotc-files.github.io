class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process(self):
        return {
            "description": self.description(),
            "values": self.process_values(),
        }

    def process_values(self):
        raise NotImplementedError()

    def description(self):
        raise NotImplementedError()

    def key_name(self):
        return None

    def value_name(self):
        return None
