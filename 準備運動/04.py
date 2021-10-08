import re
def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    s = re.sub("[,.]", "", s)
    s = s.split()
    res = dict()

    for i in range(len(s)):
        if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            res[s[i][0]] = i + 1
        else:
            res[s[i][:2]] = i + 1

    print(res)


if __name__ == "__main__":
    main()