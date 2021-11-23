from morph_class import Morph       # 別のPythonソースコードからクラスを持ってきている. 
from morph_class import Chunck      

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