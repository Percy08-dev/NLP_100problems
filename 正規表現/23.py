import json
import gzip
import re
import sys

def section_level(s: str):
    # pattern = re.compile("=+")
    sub_pattern = re.compile("[= ]+")
    n = s.count("=")
    if n%2==1:
        sys.exit()

    return "name: {}\tlevel: {}".format(re.sub(sub_pattern, "", s), n//2 - 1)

def main():
    name = "./jawiki-country.json.gz"
    with gzip.open(name, "rt", encoding="utf-8") as f:
        data = [json.loads(i) for i in f if json.loads(i)["title"] == "イギリス"]

    data:str = data[0]["text"]
    data = data.split("\n")

    # セクションの部分を切り出す. その際, 文章など不要なものが含まれないように|を除外する. 
    pattern = re.compile("(={2,}).+?\\1") 
    # 後方参照で(={2,})の部分にマッチした結果を\1から呼び出している. 
    # \1で指定する必要があるが, \はエスケープ文字なので\\で\をエスケープする必要がある
    sections = [i for i in data if re.search(pattern, i)]
    section_levels = list(map(section_level, sections))
    [print(i) for i in section_levels]

if __name__ == "__main__":
    main()