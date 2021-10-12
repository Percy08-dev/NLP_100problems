import json
import gzip
import re

def main():
    name = "./jawiki-country.json.gz"
    # gzip形式のファイルをエンコーディングutf-8で解凍
    # ここまで来たらpandasを使った方が楽？
    with gzip.open(name, "rt", encoding="utf-8") as f:
        data = [json.loads(i) for i in f if json.loads(i)["title"] == "イギリス"]
    # ここでのdataはkeys = ["title", "text"]を持つ
    # titleはイギリス, textは本文を持つ
    # text部分を取り出す. 
    data:str = data[0]["text"]
    # 改行で行を切り出す. 
    data = data.split("\n")

    pattern = re.compile("Category:")

    [print(i) for i in data if re.search(pattern, i)]



if __name__ == "__main__":
    main()