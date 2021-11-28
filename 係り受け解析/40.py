import sys

# classを使った方が速いか遅いかで言うとイメージ上遅そう. (Pythonの処理が入っている為)
class Morph:
    # メソッドを定義する際, 第一引数はそのクラスのインスタンスとなる. 
    # メンバ変数はイメージとしては構造体のメンバと同じ.
    # コンストラクタ. インスタンスを生成した際に1度だけ実行される処理. 
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
        print("surface: {:<20} base: {:<10} pos: {:<5} pos1: {:<5}".format(self.surface, self.base, self.pos, self.pos1))


def main():
    name = "ai.ja.txt.parsed"
    
    with open(name, "r", encoding="utf-8") as f:
        # 元々のテキストに * は入っていない. 
        text = []
        sentence = []
        
        for row in f:
            if row[0] == "*" or row == "\n":        # 空行とスコア行を無視
                continue 
            elif row == "EOS\n":                    # EOSで文が切れている為, 結果をtextへ追加し, 次の文用のリストを用意する.
                text.append(sentence)
                sentence = []
            else:                                   # 文の形態素を追加
                sentence.append(Morph(row))

    [[i.print() for i in sentence] for sentence in text]



if __name__ == "__main__":
    main()