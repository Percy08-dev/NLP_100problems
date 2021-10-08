def main():
    s1 = "パトカー"
    s2  ="タクシー"
    res = [s1[i//2] if i%2==0 else s2[i//2] for i in range(len(s1 + s2))]
    print("".join(res))

if __name__ == "__main__":
    main()