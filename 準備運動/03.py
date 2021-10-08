import re
def main():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    s = re.sub("[,.]", "", s)
    res = list(map(len, s.split()))
    print(res)

if __name__ == "__main__":
    main()