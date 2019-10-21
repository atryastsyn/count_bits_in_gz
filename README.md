
# count_bits_in_gz

## Count zeroes or ones in number of  gzipped binary files

A single python file that get list of folders full if binary *.gz files.
Goal is to count number of bits ('0' or '1') in all *.gz files.

Restrictions:

* we may not have enough RAM to fully unzip any given file

Algorithm:

* Iterate through arguments aka folders
* Iterate through *.gz files found in current folder
  * read file chunk by chunk
  * reduce(lambda a,b: a+b, map(lambda x: count('1'), iterable), 0)

Think about [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight)