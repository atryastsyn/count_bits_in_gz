import zlib
import os
from argparse import ArgumentParser
from functools import reduce

FILE_EXT = '.gz'
CHUNK_SIZE = 1024
BIT_TO_SEARCH = 1

parser = ArgumentParser()
parser.add_argument('folders', nargs='+', help='List of absolute paths to folders divided by space')
args = parser.parse_args()

# iterate through folders and *.gz files
def get_files_from_folder():
    for path_to_folder in (_ for _ in args.folders):
        for entry in os.listdir(path_to_folder):
            path_to_entry = os.path.join(path_to_folder, entry)
            if os.path.isfile(path_to_entry) and entry.endswith(FILE_EXT):
                yield(path_to_entry)

# iterate through files and file content chunk by chunk
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

# iterate through chunks, and map/reduce
bit_count = reduce(lambda acc, x: acc + x, map(lambda y: y.count(BIT_TO_SEARCH), get_file_content()), 0)    

print('Found {} ones'.format(bit_count))