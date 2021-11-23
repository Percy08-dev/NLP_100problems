import re
from typing import *
from morph_class import Morph       
from morph_class import Chunck      
from section4_init import init      

def root_from_noun(text:List[List[Chunck]]):
    phrase_path = []                        # 戻り値
    for sentence in text:
        for phrase in sentence:
            for word in phrase.morphs:      # 句内の名詞を確認
                if word.pos == "名詞":
                    mem = phrase            # 名詞を含む句を保存
                    break
            else:                           # breakで抜けなかった場合処理を行わない
                continue
            phrase_path.append(to_root(sentence, mem.srcs, mem.dst))

    return phrase_path 


def to_root(sentence: List[Chunck], id, next):
    path = [sentence[id].join()]
    while next != -1:                       # 末尾まで探索
        path.append(sentence[next].join())  # 句を追加
        next = sentence[next].dst           # 更新

    return path


def main():
    text = init()
    phrase_path = root_from_noun(text)

    # 出力部
    with open("out48.txt", "w", encoding="utf-8") as f:
        for i in phrase_path:
            f.write(" -> ".join(i) + "\n")



if __name__ == "__main__":
    main()