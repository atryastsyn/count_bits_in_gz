import zlib
import sys
from functools import reduce

FILE_NAME = 'test.gz'
CHUNK_SIZE = 32

d = zlib.decompressobj(16 + zlib.MAX_WBITS)

f=open(FILE_NAME,'rb')

one_count = 0


while True:
    buffer=f.read(CHUNK_SIZE)
    if not buffer:
        break
    chunk = list(d.decompress(buffer))
    ones = filter(lambda x:x==1, chunk )
    one_count += reduce(lambda x,y: x + y, filter(lambda x:x==1, chunk ))
    print(list(ones))

print(one_count)
f.close()

