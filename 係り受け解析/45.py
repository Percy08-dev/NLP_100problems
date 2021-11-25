from typing import *
from morph_class import Morph       
from morph_class import Chunck      
from section5_init import init      
import sys

def verb_case_pattern_extraction(text:List[List[Chunck]]):
    res = []
    for sentence_chunks in text:
        for phrase_data in sentence_chunks:
            index, base = predicate_info(phrase_data)
            if index == None:
                #print("@@@")
                #print([i.join() for i in sentence_chunks])
                #print("@@@")
                # sys.exit()
                continue

            particles = particle_befor_verb(sentence_chunks, index)
            if len(particles) > 0:
                res.append("{}\t{}".format(base, " ".join(particles)))   
    return res



# 最も左に現れる動詞の探索. 
# 句ごとに最左動詞を探す必要がある. 
def predicate_info(phrase_data:Chunck):
    index = None          # 動詞を含む格パターンのインデックスを保存. 
    base = ""
    for word_data in phrase_data.morphs:
        if word_data.pos == "動詞":
            index = phrase_data.srcs    # 句のIDを保管
            base = word_data.base       # 述語の基本形を保管
            break

    return index, base                      # 動詞が無かった場合, None, ""が戻される. 


# 述語に係る句の助詞を抽出
def particle_befor_verb(sentence_chunks:List[Chunck], index:int):
    res = set()

    for phrase_data in sentence_chunks:
        if phrase_data.dst != index:            # 係り受け先が述語かを確認
            continue
        for word_data in phrase_data.morphs:
            if word_data.pos == "助詞":         # 助詞を戻り値に追加
                res.add(word_data.surface)
    
    return sorted(list(res))





def main():
    text = init()
    res = verb_case_pattern_extraction(text)

    # 出力部
    with open("out45.txt", "w", encoding="utf-8") as f:
        for i in res:
            f.write(i + "\n")


if __name__ == "__main__":
    main()