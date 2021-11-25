import copy
from typing import *
from morph_class import Morph       
from morph_class import Chunck      
from section5_init import init  
from collections import deque    

# 49における変更点. 
# 戻り値の内容を辞書に変更. 
def root_from_noun(text:List[List[Chunck]]):
    path = []                          # 戻り値
    for sentence_id in range(len(text)):
        sentence = text[sentence_id]
        for phrase in sentence:
            for word in phrase.morphs:      # 句内の名詞を確認
                if word.pos == "名詞":
                    mem = phrase            # 名詞を含む句を保存
                    break
            else:                           # breakで抜けなかった場合処理を行わない
                continue
            phrase_path = {"path":to_root(sentence, mem), "sentence-id": sentence_id}    # pathにrootまでの道, sentence-idに文番号, phrase-idはpathの先頭で良いよね. 
            path.append(phrase_path)

    return path 

# 49における変更点.
# 句ではなくidでroot保存. 
def to_root(sentence: List[Chunck], phrase:Chunck):
    id = phrase.srcs
    next = phrase.dst
    
    path = [id]
    while next != -1:                       # 末尾まで探索
        path.append(next)  # 句を追加
        next = sentence[next].dst           # 更新

    return path


def shortest_pass(phrase_path:List[dict], text: List[List[Chunck]]) -> List[str]:
    res = []            # 戻り値
    for i in range(len(phrase_path)-1):
        target = phrase_path[i]
        index = i+1
        while target["sentence-id"] == phrase_path[index]["sentence-id"]:           # 同じ文の間ループ
            tmp = make_string_path(text, phrase_path, target, index)                # 最短path
            res.append(tmp)
            index += 1
            if len(phrase_path) <= index:
                break

    return res


# 最左の名詞の匿名化, 名詞をrapに置き換える. 
def noun_anonymization(phrase:Chunck, rap:str):
    res = ""
    flag = 0
    for word in phrase.morphs:
        if (flag == 1 and word.pos == "名詞") or word.pos == "記号" :   # 1つ目に出現した名詞に連続する場合は, その部分も名詞句とみなす. 記号が出現した場合も同様に名詞句の一部とみなす. 記号の出力は行わない. 
            continue
        elif word.pos == "名詞":                                        # 名詞が1つ目の名詞句の場合, rapに置換. そうでない場合何もせず文字列に追加. 
            flag += 1
            if flag == 1:                                               # rapを追加するのは1度のみ
                res += rap  
            else:                                                       # 1回目の名詞句以降の名詞
                res += word.surface
        else:
            flag += 1                                                   # 1つ目の名詞句とそれ以外を区別する為にflagを進める. 
            res += word.surface
    
    return res


def make_string_path(text: List[List[Chunck]], phrase_path:List[dict], target:dict, index:int):
    sentence_id = target["sentence-id"]
    # Xに置換する名詞句
    phrase_id = target["path"][0]
    tmp = noun_anonymization(text[sentence_id][phrase_id], "X")             
    # Yに置換する名詞句
    phrase_id = phrase_path[index]["path"][0]
    phrase_y = noun_anonymization(text[sentence_id][phrase_id], "Y")        # Yに置き換え
    if phrase_path[index]["path"][0] in target["path"]:                     # パターン1, 比較対象の名詞句が対象のpath上に存在する場合. 
        for id in target["path"][1:]:
            if id == phrase_path[index]["path"][0]:
                tmp += " -> " + phrase_y                                    # 匿名化した句を追加. Yが末尾
                break
            else:
                tmp += " -> " + text[sentence_id][id].join(exclude_symbol=True)                # pathを句に変換して追加
    else:                                                                   # パターン2
        common = set(target["path"]) & set(phrase_path[index]["path"])      # 積集合を求める. 積集合 == 共通部分
        for id in target["path"][1:]:                                       # 共通部分手前までXを含む文節を出力
            if id in common:
                tmp += " | "
                break
            else:
                tmp += " -> " + text[sentence_id][id].join(exclude_symbol=True)                # pathを句に変換して追加
        else:
            print("Error", tmp)
            input()
        
        tmp += phrase_y                                                     # Yのpathの開始
        for id in phrase_path[index]["path"][1:]:                           # 先頭以降のpathを追加
            if id in common:                                                # 共通部分の手前までを出力
                tmp += " | "
                break
            else:
                tmp += " -> " + text[sentence_id][id].join(exclude_symbol=True)                # pathを句に変換して追加

        tmp += text[sentence_id][min(common)].join(exclude_symbol=True)                        # 共通部分の先頭を追加. 

    return tmp


def main():
    text = init()
    phrase_path = root_from_noun(text)      # pathを取得
    # 49
    res = shortest_pass(phrase_path, text)  # 名詞句同士の最短Pathを取得. 
    


    # 出力部
    with open("out49.txt", "w", encoding="utf-8") as f:
        for i in res:
            f.write(i + "\n")
    
    # 問題文にある例は1459行目付近に出現. 


if __name__ == "__main__":
    main()