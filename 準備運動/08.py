def cipher(s: str):
    x = list(s)
    x = list(map(ord, x))
    x = [219 - i if 97 <= i <= 122 else i for i in x]
    x = list(map(chr, x))
    x = "".join(x)
    return x


def main():
    s = input()
    res = cipher(s)
    print(res)
    res = cipher(res)
    print(res)

if __name__ == "__main__":
    main()