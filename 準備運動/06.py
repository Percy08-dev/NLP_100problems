def chr_n_gram(s: str, n: int):
    return [s[i:i+n] for i in range(len(s) - n + 1)]

def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"
    res1 = chr_n_gram(s1, 2)
    res1 = set(res1)
    res2 = chr_n_gram(s2, 2)
    res2 = set(res2)
    print("Union", res1 | res2)
    print("Intersection", res1 & res2)
    print("Difference", res1 - res2)

    print("'se' in s1: ", "se" in res1)
    print("'se' in s2: ", "se" in res2)

if __name__ == "__main__":
    main()