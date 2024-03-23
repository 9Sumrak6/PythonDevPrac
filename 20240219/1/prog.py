import sys
import os
import zlib
import glob


def tree_parse(tree_id):
    with open(sys.argv[1] + '/.git/objects/' + tree_id[0:2] + '/' + tree_id[2:], 'rb') as tree:
        data = zlib.decompress(tree.read()).partition(b'\x00')[2]

    while data:
        name = data.partition(b'\00')[0].split(b' ')[-1].decode()
        it_id = data.partition(b'\00')[2][:20].hex()
        
        try:
            with open(sys.argv[1] + '/.git/objects/' + 
                  it_id[0:2] + '/' + it_id[2:], 'rb') as item:
                it_type = zlib.decompress(item.read()).partition(b' ')[0].decode()
        except Exception:
            print(f'blob {it_id}\t{name}')
            break

        data = data.partition(b'\00')[2][20:]
        if it_type != 'tree':
            print(f'---{it_type} {it_id}\t{name}')
        else:
            print(f'{it_type} {it_id}\t{name}')

def comm_info(data):
    for i in range(2):
        print(data[i].decode())
    for i in range(2):
        print(*data[i + 2].decode().split(' ')[:-2])
    print('\n', data[-2].decode(), '\n\n', sep='')

if len(sys.argv) == 1:
    print("There are too few arguments.")
    exit(0)

path = sys.argv[1] + '/.git/refs/heads'

if len(sys.argv) == 2:
    for item in glob.iglob(path):
        direc = os.scandir(item)

        for branch in direc:
            print(branch.name)
else:
    last_commit = open(path + '/' + sys.argv[2], "r").read()[:-1]
    
    print('Last commit info:\n')    
    with open(sys.argv[1] + '/.git/objects/' + last_commit[0:2] + '/' + last_commit[2:], "rb") as f:
        data = zlib.decompress(f.read()).partition(b'\x00')[2].split(b'\n')
        comm_info(data)

    print('\n', '.' * 57, '\n\n', 'Info about the commit tree:\n', sep='')    
    while data:
        print(f'TREE for commit {last_commit}')
        tree_parse(data[0].decode().split(' ')[1])

        if not data[3]:
            break

        last_commit = data[1].decode().split(' ')[1]
        try:
            with open(sys.argv[1] + '/.git/objects/' + 
                  last_commit[0:2] + '/' + last_commit[2:], 'rb') as commit:
                data = zlib.decompress(commit.read()).partition(b'\00')[2].split(b'\n')
        except Exception:
            break