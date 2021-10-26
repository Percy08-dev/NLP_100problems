from typing import Text
import MeCab

# neko.txt.mecabを作成する. 
def main():
    # ファイルをバッファに載せる.
    # 1MB以下なので分割はしない. 
    r_name = "./neko.txt"
    with open(r_name, "r", encoding="utf-8") as f:
        text = f.read()

    m = MeCab.Tagger("")
    res = m.parse(text)
    
    # ファイルへの書き出し
    w_name = "./neko.txt.mecab"
    with open(w_name, "w", encoding="utf-8") as f:
        f.write(res)

if __name__ == "__main__":
    main()