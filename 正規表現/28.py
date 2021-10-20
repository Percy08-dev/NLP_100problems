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
    # 今回は結合した方が楽だと思われるため, 使用するデータを1つに結合
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

# 国章画像の方に課題アリ ↓
# 内部リンクとファイルの構造が似ていることが原因 -> ファイルを除外する
def rm_ILink(o:re.Match):
    s = o.group()
    top = re.compile("\[\[ファイル:.*?]]")
    pattern1 = re.compile("\|.*(?=]])")
    # print("@@@", s, re.match(top, s))
    # ファイルリンクを除外
    if re.match(top, s) != None:
        return s 
    
    if "|" in s:
        #print("@@@1", re.search(pattern1, s).group())
        return re.search(pattern1, s).group()[1:]
    else:
        #print("@@@2", s[2:-2])
        return s[2:-2]


def rm_markup(s:str):
    # これもスタックで積んだ方が楽な気がする... 
    # {{}}の除去
    # {{}}をnon greedyで探索
    pattern1 = re.compile("\{\{.*?\}\}")
    # print("@@@", re.search(pattern1, s))
    res = re.sub(pattern1, rm_markup_c1, s)

    return res


def rm_markup_c1(o:re.Match):
    # oから文字列を{{}}を除いて取り出す.
    s = o.group()[2:-2]
    # sは{{}}の内部の文字列が格納されている. 
    # |が含まれていない物は無意味な物と考えられる為削除する. 
    # 含まれているものは, 最後の要素のみにする
    if "|" in s:
        # 文字列を|で分割し, 最後の要素を戻す
        return  s.split("|")[-1]
    else:
        return ""


def rm_htmltag(s:str):
    # non greeedly
    p = re.compile("<.*?>")
    # タグの除去
    res = re.sub(p, "", s)
    if s != res: print("@@@", s, " -> ", re.sub(p, "", s))
    
    return res


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
    pattern_27 = re.compile("\[\[.*?\]\]")
    for i in re.findall(pattern_25, template):
        row = i[1:]
        # row = row.replace(" ", "").replace("\n", "")
        row = row.replace("\n", "")
        # 26
        row = re.sub(pattern_26, rm_repl, row)
        # 27 
        row = re.sub(pattern_27, rm_ILink, row)
        # 28 MediaWikiマークアップの除去
        row = rm_markup(row)
        row = rm_htmltag(row)
        # print(row)
        row = row.split("=", 1)
        base_info[row[0]] = row[1]

    [print(i) for i in base_info.items()]
    



if __name__ == "__main__":
    main()