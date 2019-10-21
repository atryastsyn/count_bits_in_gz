import random
import gzip

FILE_LENGTH = 200
ZEROES_PROBABLITY = 95
BIN_FILE_NAME = 'test.bin'
GZ_FILE_NAME = 'test.gz'


data = []

for i in range(FILE_LENGTH):
    data.append(0 if random.randint(1,100) < ZEROES_PROBABLITY else 1)

with open(BIN_FILE_NAME, 'wb') as f:
    f.write(bytearray(data))
    f.close()

with gzip.open(GZ_FILE_NAME, 'wb') as f:
    f.write(bytearray(data))
    f.close()