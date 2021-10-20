def main():
    s = "stressed"
    #s = list(reversed(s))
    #print("".join(s))
    # こっちの方が速かった.
    print(s[::-1])

if __name__ == "__main__":
    main()