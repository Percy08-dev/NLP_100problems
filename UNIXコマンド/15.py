import io

# ファイルを末尾から読む
def tail(f: io.BufferedReader, n:int):
    chunk_size = 1024
    cnt = 0

    # 末尾へ移動
    f.seek(-1, 2)

    # ファイルサイズがチャンクサイズより小さい場合
    if chunk_size > f.tell()+1:
        f.seek(0, 0)
        data = f.read(chunk_size).decode().split()
        if n > len(data):
            for i in data:
                print(i)
        else:
            for i in reversed(range(1, n+1)):
                print(data[-i])

        return
    

    # 末尾の決定
    while True:
        # 1byte読み進む. ファイル末尾の探索. 改行等は
        # stripはデフォルトで空白を削除. 
        if f.read(1).strip() != b'':
            end = f.tell()
            break
        # 2byte 戻る
        f.seek(-2, 1)

    # 末尾から読み込み, readする分あらかじめシーク
    f.seek(end - chunk_size, 0)
    ## print(f.tell())

    # 指定数を超えるまで読み込みを続ける
    while True:
        data = f.read(chunk_size)
        str_data = data.decode()
        # 読み込んだ部分で登場した改行をカウント
        cnt += str_data.count("\n")
        # 多い分の改行が無くなるまでシークする. 
        if cnt > n:
            # 余分な行を削除する為に, readで進んだ分戻る. 
            f.seek(-chunk_size, 1)
            while cnt >= n:
                tmp = f.read(1)
                if tmp == b'\n':
                    cnt -= 1
            break
        f.seek(-chunk_size*2, 1)

    # 表示
    data = "def"
    # EOFでreadすると文字列長は0になる. 
    while len(data) > 0:
        # endで出力を終える. 
        if f.tell() + chunk_size > end:
            chunk_size = end - f.tell()
        data = f.read(chunk_size)
        data = data.decode()
        print(data, end="")



def main():
    lines = 5
    # normal
    with open("./popular-names.txt", "rb") as f:
        tail(f, lines)
    

if __name__ == "__main__":
    main()