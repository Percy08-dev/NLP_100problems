import random

def rand_swap(s: str, n:int):
    x = s.split()
    x = [string_mix(i, n) for i in x]

    return " ".join(x)

def string_mix(word: str, n:int):
    if len(word) <= n:
        return word
    else:
        word = [word[0]] + random.sample(word[1:-1], len(word[1:-1])) + [word[-1]]
        return "".join(word)

def main():
    s = input()
    res = rand_swap(s, 4)
    print(res)

if __name__ == "__main__":
    main()