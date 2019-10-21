import zlib
import sys
import os
from functools import reduce


FOLDER_PATH = os.path.join(os.getcwd(), 'storage')
FILE_EXT = '.gz'
FILE_NAME = 'test.gz'
CHUNK_SIZE = 64
BIT_TO_SEARCH = 1

decompress_object = zlib.decompressobj(16 + zlib.MAX_WBITS)

bit_count = 0

def read_generator(f, d):
    while True:
        buffer=f.read(CHUNK_SIZE)
        if not buffer:
            break
        yield list(d.decompress(buffer))

for entry in os.listdir(FOLDER_PATH):
    path_to_entry = os.path.join(FOLDER_PATH, entry)
    if os.path.isfile(path_to_entry) and entry.endswith(FILE_EXT):
        file_object = open(path_to_entry, 'rb')
        bit_count += reduce(lambda acc, x: acc + x, 
            map(lambda y: y.count(BIT_TO_SEARCH), 
                 read_generator(file_object, decompress_object)), 0)
               
        file_object.close()           

print('Found {} ones'.format(bit_count))



