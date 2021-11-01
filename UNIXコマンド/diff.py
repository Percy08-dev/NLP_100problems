import sys
import itertools
"""
def diff_botu(name1, name2):
    f1 = open(name1)
    f2 = open(name2)

    for i, j in itertools.zip_longest(f1, f2):
        row1 = i.split()
        row2 = j.split()

        if row1[0] != row2[0] or row1[1] != row2[1]:
            print(row1 + row2)

    f1.close()
    f2.close()
"""

# 値のみでdiff
def diff(name1, name2):
    with open(name1) as f:
        data1 = f.readlines()
        data1 = [i.split() for i in data1]
        # 2列目でソートした後に1列目でソート
        data1 = sorted(sorted(data1, key=lambda x:x[1]), key=lambda x:int(x[0]))

    with open(name2) as f:
        data2 = f.readlines()
        data2 = [i.split() for i in data2]
        data2 = sorted(sorted(data2, key=lambda x:x[1]), key=lambda x:int(x[0]))

    # diff
    for i, j in itertools.zip_longest(data1, data2):
        if i != j:
            print(i, j)

    



def main():
    names = sys.argv
    diff(names[1], names[2])

if __name__ == "__main__":
    main()