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

    # patternの文字列を持つ行を抽出する. 
    pattern = re.compile("Category:")
    categorys = [i for i in data if re.search(pattern, i)]
    ## [print(i) for i in categorys]
    # Categoryの右側を抽出. この時最後は]という条件を付けることで, 0番目の要素を除く. 
    pattern = re.compile(":.*]")
    category_names = [re.search(pattern, i) for i in categorys]
    # 先頭の:を除去
    category_names = [i.group()[1:] for i in category_names if i != None]
    # この正規表現の意味: *か|か]のいずれか
    # subでこの正規表現にマッチする物を""と置き換える. 
    pattern = re.compile("[*|\||\]]")
    category_names = [re.sub(pattern, "", i) for i in category_names]
    [print(i) for i in category_names]



if __name__ == "__main__":
    main()