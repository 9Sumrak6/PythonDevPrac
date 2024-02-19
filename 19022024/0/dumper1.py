import glob
import zlib


for i in glob.iglob(input() + "/??/*", recursive=True):
    print(type(i), i)
