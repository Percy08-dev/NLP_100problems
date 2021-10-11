def data_processing(row: str)->list:
    # 文字列を空白で分割し, そのリストを得る. 
    row = row.split()
    row[2] = int(row[2])
    row[3] = int(row[3])
    return row


def main():
    # ファイルがメモリに乗る程度の大きさの場合
    # 乗らないほど大きな物はマージソートの要領でソート
    name = "./popular-names.txt"
    with open(name, "r") as f:
        # リスト内包表記で, 関数の戻り値をリストに保存
        data = [data_processing(i) for i in f]
        # ラムダ式でリストの3番目の要素を取り出し, その要素をキーに降順ソート
        data.sort(key=lambda x:x[2], reverse=True)

    [print(*i) for i in data]

if __name__ == "__main__":
    main()