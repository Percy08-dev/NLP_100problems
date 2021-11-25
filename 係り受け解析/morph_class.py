# 第4章 係り受け解析で使用するクラスをまとめたファイル. 
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
        print("surface:{}\tbase:{}\tpos:{}\tpos1:{}".format(self.surface, self.base, self.pos, self.pos1))


# 
class Chunck:
    def __init__(self, morphs:List[Morph], dst, srcs) -> None:
        self.morphs = morphs    # 形態素
        self.dst = dst          # 係り受け先インデックス
        self.srcs = srcs        # 係り受け元インデックス

    # 以下メソッド
    def join(self, sep = "", start = 0, end = None, exclude_symbol = False)->str:
        res = ""
        for i in self.morphs[start:end]:
            if exclude_symbol and i.pos == "記号":
                continue
            res += i.surface
        return res
