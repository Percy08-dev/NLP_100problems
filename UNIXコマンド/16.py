import os
import sys
def file_split(name: str, n:int):
    # 分割したファイルを保存するディレクトリ
    div = "./div/"
    # 作業ディレクトリの作成
    if not os.path.exists(div):
        os.mkdir(div)
    with open(name, "rb") as f:
        # ファイルに含まれる行数のカウント
        line_cnt = sum([1 for _ in f])
        # 1ファイルあたりの行数
        num = line_cnt // n
        # 分配が必要なあまり
        mod = line_cnt % n
        f.seek(0, 0)
        # データ量が大きい場合は以下をを変更
        data = f.readlines()
        data = [i.decode() for i in data]

    for i in range(n):
        name = div + str(i) + ".txt"
        print(name)
        
        with open(name, "w") as wf:
            if i < mod:
                wf.writelines(data[num*i:num*(i+1) + 1])
            else:
                wf.writelines(data[num*i:num*(i+1)])



def main():
    n = sys.argv
    n = int(n[1])
    name = "./popular-names.txt"
    file_split(name, n)

if __name__ == "__main__":
    main()