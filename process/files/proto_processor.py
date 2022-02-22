from files.file_processor import FileProcessor


class ProtoProcessor(FileProcessor):
    def __init__(self, file_path):
        super().__init__(file_path)

    def process_proto(self, _):
        raise NotImplementedError()

    def proto_template(self):
        raise NotImplementedError()

    def process_values(self):
        with open(self.file_path, 'rb') as f:
            proto = self.proto_template()
            proto.ParseFromString(f.read())
            return self.process_proto(proto)
