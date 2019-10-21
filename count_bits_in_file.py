import zlib
import sys
from functools import reduce

FILE_NAME = 'test.gz'
CHUNK_SIZE = 32

decompress_object = zlib.decompressobj(16 + zlib.MAX_WBITS)

file_object = open(FILE_NAME,'rb')

bit_count = 0

def read_generator(f):
    while True:
        buffer=f.read(CHUNK_SIZE)
        if not buffer:
            break
        yield list(decompress_object.decompress(buffer))

bit_count = reduce(lambda x, y: x + y, map(lambda x: x.count(1), read_generator(file_object)))

print (bit_count)

file_object.close()

