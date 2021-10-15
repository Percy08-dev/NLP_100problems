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


def regex(data):
    # 今回は結合した方が楽だと思われるため, 使用するデータを1津に結合
    s = "\n".join(data)
    # {{基礎情報 hogehoge\n から始まり, |hogehoge若しくは*hogehogeにマッチする行を次の行が}}\nになるまで探索する正規表現. 
    # ※hogehogeには何かしらの文字列が入る
    pattern = re.compile("\{\{基礎情報.*\n((\|.*\n)|(\*.*\n))*}}\n")
    res = re.search(pattern, s).group()
    # print(res)
    return res



def rm_repl(o:re.Match):
    s = o.group()
    s = s.replace("\'", "")
    return s
    

def main():
    name = "./jawiki-country.json.gz"
    with gzip.open(name, "rt", encoding="utf-8") as f:
        data = [json.loads(i) for i in f if json.loads(i)["title"] == "イギリス"]

    data:str = data[0]["text"]
    data = data.split("\n")

    template = regex(data)
    template = put_in_order(template)
    base_info = dict()
    pattern_25 = re.compile("\|.*=.*\n(?=\||})")
    pattern_26 = re.compile("\'{2,5}.*\'{2,5}")
    for i in re.findall(pattern_25, template):
        row = i[1:]
        # row = row.replace(" ", "").replace("\n", "")
        row = row.replace("\n", "")
        row = re.sub(pattern_26, rm_repl, row)
        row = row.split("=", 1)
        base_info[row[0]] = row[1]

    
    [print(i) for i in base_info.items()]



if __name__ == "__main__":
    main()