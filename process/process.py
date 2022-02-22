import os
import json

from files.processor_mapping import find_processor
from pages.processor_list import page_processor_list


def main():
    files = os.listdir('./raw')
    unrecognized_files_count = 0
    processed_files_count = 0
    bad_files_count = 0
    file_data_dict = {}
    for f in files:
        file_name_components = f.split('.')
        if len(file_name_components) != 3:
            bad_files_count += 1
            continue
        [name, _, extension] = file_name_components
        id_processor_pair = find_processor(name, extension)
        if id_processor_pair:
            id, processor_class = id_processor_pair
            processed_files_count += 1
            processor = processor_class('./raw/' + f)
            processed_result = processor.process()
            if processor.key_name():
                file_data_dict[id] = dict(
                    [(
                        value[processor.key_name()],
                        value[processor.value_name(
                        )] if processor.value_name() else value
                    )
                        for value in processed_result["values"]])
            else:
                file_data_dict[id] = processed_result["values"]
            json.dump(processed_result,
                      open('./data/' + id + '.json', 'w'), indent=2, sort_keys=True)
        else:
            unrecognized_files_count += 1
    for id, processor_class in page_processor_list():
        processor = processor_class(file_data_dict)
        processed_result = processor.process()
        json.dump(processed_result,
                  open('../src/data/' + id + '.json', 'w'), indent=2, sort_keys=True)
    print('Unrecognized files: %d, processed files: %d' %
          (unrecognized_files_count, processed_files_count))


if __name__ == '__main__':
    main()
