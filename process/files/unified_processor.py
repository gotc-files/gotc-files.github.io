from files.proto_processor import ProtoProcessor
from files.json_processor import JsonProcessor


class UnifiedProcessor(ProtoProcessor, JsonProcessor):
    def process_values(self):
        if self.file_path.endswith(".json"):
            return JsonProcessor.process_values(self)
        elif self.file_path.endswith(".pb"):
            return ProtoProcessor.process_values(self)
