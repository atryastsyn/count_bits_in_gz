import zlib
import sys

FILE_NAME = 'test.gz'
CHUNK_SIZE = 32

d = zlib.decompressobj(16 + zlib.MAX_WBITS)

f=open(FILE_NAME,'rb')
buffer=f.read(CHUNK_SIZE)

while buffer:
  chunk = list(d.decompress(buffer))
  print(chunk)
  
  buffer=f.read(CHUNK_SIZE)


f.close()

