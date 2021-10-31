def main():
    with open("./popular-names.txt", "r") as f:
        data = f.readlines()
    print(len(data))

# あまり使用しない
def temp():
    f = open("./popular-names.txt", "r")
    data = f.readlines()
    f.close()
    print(len(data))

if __name__ == "__main__":
    main()