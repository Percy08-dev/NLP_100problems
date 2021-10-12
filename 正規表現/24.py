import json
import gzip
import re

def f1(o: re.Match):
    # :から始まり, |か]で終わる最短のパターン
    pattern = re.compile(":.*?(\||])")
    s = o.group()
    index = re.search(pattern, s)
    # indexに正規表現がマッチした位置が記録されている. startメソッドは開始位置, endメソッドは終了位置のオフセットを返す. 
    # 両端に余分な要素がある為, 1ずつ要素を縮めて返す. 
    return s[index.start()+1:index.end()-1]


def main():
    name = "./jawiki-country.json.gz"
    with gzip.open(name, "rt", encoding="utf-8") as f:
        data = [json.loads(i) for i in f if json.loads(i)["title"] == "イギリス"]

    data:str = data[0]["text"]
    data = data.split("\n")

    # file(大文字小文字無視):かファイル:から始まり, ]で終わるパターン
    pattern = re.compile("(file|ファイル):.*]", re.I)
    media = [re.search(pattern, i) for i in data]
    media = [f1(i) for i in media if i != None]

    [print(i) for i in media]

if __name__ == "__main__":
    main()