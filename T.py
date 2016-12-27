#!/usr/local/bin/python3
from sys import stdin, argv

__doc__ = """
Usage:
    T
    join [-h | --help]

Options:
    -h --help       Show this screen and exit.

Note:
    行と列を入れ替える(転置).
"""

def usage():
    print(__doc__)
    exit()

def main():
    data = [ row.strip().split() for row in stdin.readlines() ]
    column_max = max( [len(row) for row in data] )
    for _ in range(column_max):
        for elm in data:
            try: print(elm[_], end=' ')
            except: print('-', end=' ')
        print()



if __name__ == '__main__':
    for v in argv[1:]:
        if v in ['-h', '--help']:
            usage()
    main()