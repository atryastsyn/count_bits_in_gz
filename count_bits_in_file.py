import zlib
import sys

FILE_NAME = 'test.gz'
CHUNK_SIZE = 32

d = zlib.decompressobj(16 + zlib.MAX_WBITS)

f=open(FILE_NAME,'rb')

while True:
    buffer=f.read(CHUNK_SIZE)
    if not buffer:
        break
    chunk = list(d.decompress(buffer))
    print(chunk)


f.close()
