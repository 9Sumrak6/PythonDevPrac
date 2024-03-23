#import sys
import zlib


f = input()
with open('../../.git/objects/' + f, "rb") as f1:
    content = f1.read()

print(zlib.decompress(content))
#zlib.decompress()
