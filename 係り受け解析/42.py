from typing import *

# classを使った方が速いか遅いかで言うとイメージ上遅そう. (Pythonの処理が入っている為)
class Morph:
    # メソッドを定義する際, 第一引数はそのクラスのインスタンスとなる. 
    # メンバ変数はイメージとしては構造体のメンバと同じ.
    # コンストラクタ. クラスを生成した際に1度だけ実行される処理. 
    def __init__(self, morphs:str) -> None:
        # 前処理
        surface, others = morphs.split("\t")
        others = others.split(",")
        # メンバ変数の定義
        self.surface = surface
        self.base = others[6]
        self.pos = others[0]
        self.pos1 = others[1]
    # 以下でメソッドの定義も可能. 
    # 表示用メソッド. 
    def print(self):
        print("surface:{}\t base:{}\t pos:{}\t pos1:{}".format(self.surface, self.base, self.pos, self.pos1))


# 
class Chunck:
    def __init__(self, morphs:List[Morph], dst, srcs) -> None:
        self.morphs = morphs    # 形態素
        self.dst = dst          # 係り受け先インデックス
        self.srcs = srcs        # 係り受け元インデックス

    # 以下メソッド
    def join(self, sep = ""):
        res = ""
        for i in self.morphs:
            res += i.surface
        return res


def init():
    name = "ai.ja.txt.parsed"
    
    with open(name, "r", encoding="utf-8") as f:
        text = []
        sentence = []
        phrase = []

        for row in f:
            if row == "\n":
                continue
            elif row[0] == "*":
                # 文のはじめに対応. ダミーを加えるのとどっちが速い？
                if type(phrase) == list:
                    # 新しい文節の構成
                    tmp = row.split()
                    dst = int(tmp[2][:-1])
                    srcs = int(tmp[1])
                    phrase = Chunck([], dst, srcs)
                else:
                    # 文節の記録. 
                    sentence.append(phrase)
                    # 新しい文節の構成
                    tmp = row.split()
                    dst = int(tmp[2][:-1])
                    srcs = int(tmp[1])
                    phrase = Chunck([], dst, srcs)
            elif row == "EOS\n":
                # 文節の保存
                sentence.append(phrase)
                # 文の保存
                text.append(sentence)
                
                # 初期化
                sentence = []
                phrase = []
            else:
                # 文節へ単語の追加
                phrase.morphs.append(Morph(row))

    return text


def main():
    text = init()   #41 の処理を行う. 

    for sentence in text:
        for phrase in sentence:
            # 係り元出力
            for word in phrase.morphs:
                if word.pos != "記号":
                    print(word.surface, end = "")
            print("\t", end = "")

            # 係り先出力
            for word in sentence[phrase.dst].morphs:
                if word.pos != "記号":
                    print(word.surface, end = "")
            print("\t")

if __name__ == "__main__":
    main()