from os import waitpid
import MeCab
import re
from typing import List

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


def verb_extractor(data:List[List[dict]]) -> list:
    # 動詞の表層型のリストを求める. 
    # 重複する要素は必要ないと考えられる為, set型を用いる. 
    res = set()

    # 文書 -> 文 -> 単語 -> 形態素の構造になっている.
    # 単語ごとに処理を行う. 
    for sentence in data:
        for morphemes in sentence:
            if morphemes["pos"] == "動詞":
                res.add(morphemes["surface"])

    return list(res)    # 集合型をリストに変換. 順序は毎回異なる可能性がある. 


def main():
    name = "./neko.txt.mecab"       # ファイル名
    data = init(name)               # 30までの処理を行う. 
    verbs = verb_extractor(data)    # 31の処理

    print(len(verbs))





if __name__ == "__main__":
    main()