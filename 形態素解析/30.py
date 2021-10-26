import MeCab
import re

def main():
    # ファイルをバッファに載せる.
    # ファイルサイズは11MB程. 
    # 1行ずつ処理を行う.  
    # 1行ごとに単語及びその形態素が記録されている. 
    # MeCabの出力の各見出しは, 表層型, 品詞, 品詞細分類1, 品詞細分類2, 品詞細分類3, 活用形, 活用型, 原型, 読み, 発音の順に出力される. 
    # 課題 -> 段落番号の扱い. 現在は文に含まれている. 

    name = "./neko.txt.mecab"   # ファイル名
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

    for i in res[:10]:
        for j in i:
            print(j)
        print()


if __name__ == "__main__":
    main()