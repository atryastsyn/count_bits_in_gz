import random
import gzip
import os
import argparse

FILE_LENGTH = 2048
ZEROES_PROBABLITY = 99
FOLDER_TEMPLATE = 'storage_{}'
FOLDER_COUNT = 8
FILE_TEMPLATE = 'zeroes_and_ones_{}.gz'
FILE_COUNT = 32

parser = argparse.ArgumentParser()
parser.add_argument('base_folder', help='Absolute path to base folder where folders and gzipped files will be created')
args = parser.parse_args()

for i in range(FOLDER_COUNT):
    folder_path = os.path.join(args.base_folder, FOLDER_TEMPLATE.format(str(i)))
    if not os.path.exists(folder_path):
        # create folder
        os.mkdir(folder_path)
    else:
        # remove content from existing folder
        for entry in os.listdir(folder_path):
            path_to_entry = os.path.join(folder_path, entry)
            if os.path.isfile(path_to_entry):
                os.remove(os.path.join(path_to_entry))

    # create binary gzipped files
    for j in range(FILE_COUNT):
        file_path = os.path.join(folder_path, FILE_TEMPLATE.format(str(j)))
        data = [0 if random.randint(1,100) < ZEROES_PROBABLITY else 1 for _ in range(FILE_LENGTH)]
        with gzip.open(file_path, 'wb') as f:
            f.write(bytearray(data))
            f.close()
