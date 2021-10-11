def main():
    name = "./popular-names.txt"
    # 1列目の文字列を保存する変数
    res = set()
    with open(name, "r") as f:
        # ファイルオブジェクト
        for row in f:
            # 取得した行を分離し, 生成されたリストの先頭を返す. 
            res.add(row.split()[0])

    # set型に順番はない為, listに変換しsort
    res = sorted(list(res))
    print(res)

if __name__ == "__main__":
    main()