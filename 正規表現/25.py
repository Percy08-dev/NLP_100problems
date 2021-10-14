import json
import gzip
import re

# 正規表現よりもスタックで積んだ方が楽な気がしたので作ってみました. 
# {}で解析を掛けて, はじめの基礎情報に掛かっていた{}が終了したら終了する. 
def stuck(data:list):
    s = []
    res = ""
    start = -1
    for i in range(len(data)):
        if "基礎情報" in data[i]:
            start = i
            break

    for i in data[start:]:
        for j in i:
            if j == "{":
                s.append(j)
            elif j == "}":
                s.pop(-1)
            
            res += j

            if len(s) == 0:
                break
        else:
            res += "\n"
            continue
        break

    return res


# スタックで実装
def stuck_analyze(data):
    template = stuck(data)
    print(template)
    return template


def regex(data):
    # 今回は結合した方が楽だと思われるため, 使用するデータを1津に結合
    s = "\n".join(data)
    # {{基礎情報 hogehoge\n から始まり, |hogehoge若しくは*hogehogeにマッチする行を次の行が}}\nになるまで探索する正規表現. 
    # ※hogehogeには何かしらの文字列が入る
    pattern = re.compile("\{\{基礎情報.*\n((\|.*\n)|(\*.*\n))*}}\n")
    res = re.search(pattern, s).group()
    print(res)
    return res


def main():
    name = "./jawiki-country.json.gz"
    with gzip.open(name, "rt", encoding="utf-8") as f:
        data = [json.loads(i) for i in f if json.loads(i)["title"] == "イギリス"]

    data:str = data[0]["text"]
    data = data.split("\n")

    print("0: 正規表現で実装\n1: stuckで実装")
    print("0 or 1: ", end = "")
    x = int(input())
    if x:
        # スタック
        stuck_analyze(data)
    else:
        # 正規表現  
        regex(data)

    


if __name__ == "__main__":
    main()