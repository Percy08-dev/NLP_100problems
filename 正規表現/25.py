import json
import gzip
import re

def put_in_order(template:str):
    # templateの整形. 複数行に分かれている物をtempate = valueの形に整形する. 
    tmp = []
    for i in template.split("\n")[1:]:
        if len(i) == 0: continue
        if i[0] == "|":
            tmp.append(i)
        else:
            tmp[-1] += i

    return "\n".join(tmp)


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
    # print(template)
    return template


def regex(data):
    # 今回は結合した方が楽だと思われるため, 使用するデータを1津に結合
    s = "\n".join(data)
    # {{基礎情報 hogehoge\n から始まり, |hogehoge若しくは*hogehogeにマッチする行を次の行が}}\nになるまで探索する正規表現. 
    # ※hogehogeには何かしらの文字列が入る
    pattern = re.compile("\{\{基礎情報.*\n((\|.*\n)|(\*.*\n))*}}\n")
    res = re.search(pattern, s).group()
    # print(res)
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
        template = stuck_analyze(data)
    else:
        # 正規表現  
        template = regex(data)
    
    # templateの整形. (複数行に渡る正規表現はめんどくさい)
    template = put_in_order(template)

    # 辞書型にしまう
    base_info = dict()
    # |で始まり, 改行コードの次に|若しくは}が来ているものにヒットする正規表現
    # 複数行に対応できていない.  -> 複数行にまたがっているものを連結する. 
    # pattern = re.compile("\|.*=.*\n")
    pattern = re.compile("\|.*=.*\n(?=\||})")
    for i in re.findall(pattern, template):
        # |を除去
        row = i[1:]
        # 空白を削除 -> 英語混じりだからしない方が良いかも
        # row.replace(" ", "")
        # =で分割
        row = row.split("=", 1)
        # 辞書に追加
        base_info[row[0]] = row[1]

    [print(i) for i in list(base_info.items())]



if __name__ == "__main__":
    main()