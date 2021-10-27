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


def noun_phrase_extractor(data:List[List[dict]]) -> list:
    res = set()

    for sentence in data:
        # 3単語1組で見ていくため, n単語の文ならばn-2回移動が必要である. 
        for i in range(len(sentence) - 2):
            if sentence[i]["pos"] == "名詞" and sentence[i+1]["surface"] == "の" and sentence[i+2]["pos"] == "名詞":
                res.add(sentence[i]["surface"] + sentence[i+1]["surface"] + sentence[i+2]["surface"])

    return list(res)


def main():
    name = "./neko.txt.mecab"       # ファイル名
    data = init(name)               # 30までの処理を行う. 
    phrase = noun_phrase_extractor(data)

    print(len(phrase))
    print(phrase[0:10])





if __name__ == "__main__":
    main()