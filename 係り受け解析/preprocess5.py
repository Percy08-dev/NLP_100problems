import CaboCha
import zipfile
import itertools

def main():
    # ファイルを展開. 
    name = "./ai.ja.zip"
    with zipfile.ZipFile(name) as f:
        # zipファイルに内包されているファイルを確認. 
        names = f.namelist()
        print(names)
        # 今回はメモリ上で処理を行う. 
        # 今回はopenではなくzipfileで開いている. 
        # ファイルを読み込む. (バイナリ)
        data = f.read(names[0])
    
    # デコード
    data = data.decode()


    # CaboChaは、文ごとに区切ったデータを与える. 
    # 区切らない場合, 巨大な解析木を生成する. 
    # 行ごとに分割. 
    data = data.split("\n")
    
    # 空行を削除
    data = [i for i in data if len(i) > 0]

    # 行に複数の文を含む場合がある為, それらを分割
    data = [i.split("。") for i in data]

    # 二次元配列を一次元に
    data = list(itertools.chain.from_iterable(data))

    # 空行を削除
    data = [i for i in data if len(i) > 0]

    # ChaboChaで解析
    # パーサーオブジェクトを定義
    c = CaboCha.Parser()
    
    with open("ai.ja.txt.parsed", "w", encoding="utf-8") as f:
        for i in data:
            # 解析  
            res = c.parse(i)
            # 扱いやすい形へ整形
            res = res.toString(CaboCha.FORMAT_LATTICE)

            # 書き込み 改行要らないかも
            f.write(res + "\n")



if __name__ == "__main__":
    main()