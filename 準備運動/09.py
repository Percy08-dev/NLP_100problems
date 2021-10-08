import random

def rand_swap(s: str, n:int):
    x = s.split()
    x = list(map(list, x))

    for word in x:
        if len(word) <= n:
            continue
        for i in range(1, len(word) - 2):
            rnum = random.randint(1, len(word)-2)
            word[i], word[rnum] = word[rnum], word[i]
    
    x = list(map("".join, x))
    return x

def main():
    s = input()
    res = rand_swap(s, 4)
    print(res)

if __name__ == "__main__":
    main()