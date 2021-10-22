def main():
    s = "パタトクカシーー"
    # new = [s[i] for i in range(len(s)) if i%2==0]
    # print("".join(new))
    new = s[::2]
    print(new)

if __name__ == "__main__":
    main()