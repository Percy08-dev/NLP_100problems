import pandas as pd
import copy

from pandas.io.parsers import read_table

def vartical_marge(*cols, sep = " "):
    data = copy.deepcopy(list(cols))
    res = data.pop()
    if len(data) == 0:
        return res
    
    for _ in range(len(data)):
        res = [j.replace("\n", sep) + i for i, j in zip(res, data.pop())]

    return res



def main():
    """
    # 遅い!!!
    col1 = pd.read_table("./col1.txt")
    col2 = pd.read_table("./col2.txt")
    data = pd.concat([col1, col2], axis=1)
    data.to_csv("./new.txt", sep = "\t", index=False)
    print(data.head())
    """

    with open("./col1.txt", "r") as f:
        col1 = f.readlines()
    with open("./col2.txt", "r") as f:
        col2 = f.readlines()

    data = vartical_marge(col1, col2, sep="\t")
    
    with open("./new.txt", "w") as f:
        f.writelines(data)


if __name__ == "__main__":
    main()