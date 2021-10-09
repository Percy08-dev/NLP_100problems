def main():
    with open("./popular-names.txt", "r") as f:
        data = f.readlines()
    print(len(data))

if __name__ == "__main__":
    main()