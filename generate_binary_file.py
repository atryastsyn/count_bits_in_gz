import random
import gzip
import os


FILE_LENGTH = 2048
ZEROES_PROBABLITY = 99
FOLDER_PATH = os.path.join(os.getcwd(), 'storage')
FILE_TEMPLATE = 'test{}.gz'
FILE_COUNT = 24


if not os.path.exists(FOLDER_PATH):
    # create folder
    os.mkdir(FOLDER_PATH)
else:
    # remove content from existing folder
    for entry in os.listdir(FOLDER_PATH):
        path_to_entry = os.path.join(FOLDER_PATH, entry)
        if os.path.isfile(path_to_entry):
            os.remove(os.path.join(path_to_entry))

for i in range(FILE_COUNT):
    file_path = os.path.join(FOLDER_PATH, FILE_TEMPLATE.format(str(i)))
    data = [0 if random.randint(1,100) < ZEROES_PROBABLITY else 1 for _ in range(FILE_LENGTH)]
    with gzip.open(file_path, 'wb') as f:
        f.write(bytearray(data))
        f.close()
    