from typing import *
from morph_class import Morph       # 別のPythonソースコードからクラスを持ってきている. 
from morph_class import Chunck      
from section4_init import init      
from graphviz import Digraph        # グラフ描写用.

# 文の係り受け解析結果を有向グラフで表す.
def Dependencies(sentence:List[Chunck]):
    graph = Digraph(format="png")               # グラフのオブジェクト
    graph.attr('node', fontname='MS Gothic')    # 日本語用フォントの指定

    table = dict()                              # ChunkのIDでノードの繋がりを指定する為のテーブル. Key = ID, Value = phrase

    # nodeの名前で繋ぐ部分を指定する必要がある為, nodeに句を使用した場合ChunkのIDが使えなくなる. 
    for phrase_data in sentence:
        phrase = phrase_data.join() + "({})".format(phrase_data.srcs)   # 句の文字列を取り出すし, IDを句の末尾に付与する. 
        graph.node(phrase)                                              # グラフオブジェクトにノードを追加する. 
        table[phrase_data.srcs] = phrase                                # IDとノード名の対応
    
    for phrase_data in sentence:
        if phrase_data.dst == -1:
            continue
        graph.edge(table[phrase_data.srcs], table[phrase_data.dst])     # エッジを描く. テーブルをもとにIDからphraseへの変換を行う. 

    graph.render("image/output")                # レンダリング
    graph.view()



def main():
    text = init()
    # [print(i.srcs, i.dst) for i in text[1]]
    Dependencies(text[1])   # グラフ描写. 



if __name__ == "__main__":
    main()