def word_n_gram(s: str, n: int):
    x = s.split()
    return [x[i:i+n] for i in range(len(x) - n + 1)]

def chr_n_gram(s: str, n: int):
    return [s[i:i+n] for i in range(len(s) - n + 1)]

def main():
    s = "I am an NLPer"
    words = word_n_gram(s, 2)
    chrs = chr_n_gram(s, 2)
    print(words)
    print(chrs)
    

if __name__ == "__main__":
    main()