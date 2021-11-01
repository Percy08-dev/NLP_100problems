def main():
    name = "./popular-names.txt"
    # 辞書型で解答を保存
    res = dict()
    with open(name, "r") as f:
        # ファイルから1行ずつ取り出す
        for i in f:
            # 1列目の要素を取得
            col1 = i.split()[0]
            # 辞書型に1列目の要素がkeyに存在すれば +1. 無ければ, keyを追加し, valueは１
            if col1 in res:
                res[col1] += 1
            else:
                res[col1] = 1

    # 辞書型のresからメソッドitemsでkeyとvalueのタプルを取得, そのタプルの1つ目の要素をキーに降順ソート
    res = sorted(res.items(), key= lambda x: x[1], reverse=True)

    # [print(*i) for i in res]
    [print("\t".join(map(str, reversed(i)))) for i in res]


if __name__ == "__main__":
    main()
