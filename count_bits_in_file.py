import zlib
import sys
import os
from functools import reduce


FOLDER_PATH = os.path.join(os.getcwd(), 'storage')
FILE_EXT = '.gz'
CHUNK_SIZE = 64
BIT_TO_SEARCH = 1


# iterate through *.gz files in given folder
def get_files_from_folder():
    for entry in os.listdir(FOLDER_PATH):
        path_to_entry = os.path.join(FOLDER_PATH, entry)
        if os.path.isfile(path_to_entry) and entry.endswith(FILE_EXT):
            yield(path_to_entry)

# iterate through file chunk by chunk
def get_file_content():
    for path_to_file in get_files_from_folder():
        file_object = open(path_to_file, 'rb')
        decompress_object = zlib.decompressobj(16 + zlib.MAX_WBITS)
        while True:
            buffer=file_object.read(CHUNK_SIZE)
            if not buffer:
               file_object.close() 
               break
            yield list(decompress_object.decompress(buffer))

bit_count = reduce(lambda acc, x: acc + x, map(lambda y: y.count(BIT_TO_SEARCH), get_file_content()), 0)    

print('Found {} ones'.format(bit_count))