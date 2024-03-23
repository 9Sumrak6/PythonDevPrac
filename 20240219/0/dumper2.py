import glob
import zlib


for i in glob.iglob(input() + "/??/*"):
    f = open(i, "rb")
    a = zlib.decompress(f.read())
    if a[4] == 105:
        print(i)
