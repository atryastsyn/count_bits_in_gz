import zlib
import sys
from functools import reduce

FILE_NAME = 'test.gz'
CHUNK_SIZE = 32
BIT_TO_SEARCH = 1

decompress_object = zlib.decompressobj(16 + zlib.MAX_WBITS)
file_object = open(FILE_NAME,'rb')
bit_count = 0

def read_generator(f, d):
    while True:
        buffer=f.read(CHUNK_SIZE)
        if not buffer:
            break
        yield list(d.decompress(buffer))

bit_count = reduce(lambda x, y: x + y, map(lambda x: x.count(BIT_TO_SEARCH), read_generator(file_object, decompress_object)))

print (bit_count)

file_object.close()

