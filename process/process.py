import json
import os
import sys

from files.processor_mapping import find_processor
from pages.processor_list import page_processor_list
from data_manager import DataManager


def main():
    if len(sys.argv) < 2:
        print('Please specify the raw data directory')
    raw_data_dir = sys.argv[1]
    files = os.listdir(raw_data_dir)
    unrecognized_files_count = 0
    processed_files_count = 0
    bad_files_count = 0
    context = {
        "file_lookup_dict": {},
        "file_values_dict": {},
    }
    data_manager = DataManager()
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
            processor = processor_class(os.path.join(raw_data_dir, f))
            processed_result = processor.process()
            data_manager.add_file_data(
                id, processed_result["values"], processor.key_names(), processor.value_name())
            json.dump(processed_result,
                      open('./data/' + id + '.json', 'w'), indent=2, sort_keys=True)
        else:
            unrecognized_files_count += 1
    for id, processor_class in page_processor_list():
        processor = processor_class(data_manager)
        processed_result = processor.process()
        json.dump(processed_result,
                  open('../src/data/' + id + '.json', 'w'), indent=2, sort_keys=True)
    print('Unrecognized files: %d, processed files: %d' %
          (unrecognized_files_count, processed_files_count))


if __name__ == '__main__':
    main()
