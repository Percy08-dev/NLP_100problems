import re
from typing import *
import matplotlib.pyplot as plt


def init(name:str):
    res = []                    # sentenceを集めたリスト(解答保存用)
    sentence = []               # 1文ごとの辞書型の保管
    sep = re.compile("[\t,]")   # 形態素分割用のセパレータ
    with open(name, "r", encoding="utf-8") as f:
        for row in f:
            if "EOS" in row: 
                continue   # EOSはスキップ
            morpheme = re.split(sep, row[:-1])  # 形態素を要素ごとに分割する. セパレータを複数指定する為にreを使用. 末尾に改行が含まれる. 
            temp = {"surface":morpheme[0], "base":morpheme[7], "pos":morpheme[1], "pos1":morpheme[2]}   # 形態素を保存する辞書型
            sentence.append(temp)               # appendはO(1)だが定数倍が大きい為繰り替えと時間がかかる. 

            if "。" in temp["surface"]:         # 表層型に句点(。)がある場合は, 文を区切る.
                res.append(sentence)            # sentenceをresに追加し, sentenceを初期化する. 
                sentence = []
        
        

    return res


def word_counter(data:List[List[dict]]) -> list:
    # 出現数はkey = word, value = countの形で辞書型に保存する. 
    res = dict()

    for sentence in data:
        for morphemes in sentence:
            # 記号は単語では無い. 
            if morphemes["pos"] == "記号":
                continue
            # 単語を取り出す. 
            word = morphemes["surface"]
            # 単語が既出であればincrement, 無ければ1. 
            if word in res:
                res[word] += 1
            else:
                res[word] = 1
    
    # 辞書からkeyとvalueをセットで取り出す. 
    # 形式は[(key0, value0), (key1, value1), ...]の形式. (リストの内部にタプルが入っている. タプルにはkeyとvalueがセットで入っている. )
    # これはclass dict_itemsなのでlistに変換する. 
    res = res.items()
    return list(res)


def log_plot_drow(x_data, y_data):
    # 描写
    plt.plot(x_data, y_data)
    # スケール変更
    plt.xscale("log")
    plt.yscale("log")

    plt.grid()
    plt.show()


def main():
    name = "./neko.txt.mecab"       # ファイル名
    data = init(name)               # 30までの処理を行う. 
    word_counts = word_counter(data)# 単語の出現数を算出
    word_counts.sort(key = lambda x:x[1], reverse=True)
    # x軸は順位
    x_data = [i+1 for i in range(len(word_counts))]
    # y軸は出現回数
    y_data = [i[1] for i in word_counts]
    log_plot_drow(x_data, y_data)


if __name__ == "__main__":
    main()