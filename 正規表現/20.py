import json
import gzip

def main():
    name = "./jawiki-country.json.gz"
    # gzip形式のファイルをエンコーディングutf-8で解凍
    # ここまで来たらpandasを使った方が楽？
    with gzip.open(name, "rt", encoding="utf-8") as f:
        data = [json.loads(i) for i in f if json.loads(i)["title"] == "イギリス"]
        print(data)

if __name__ == "__main__":
    main()