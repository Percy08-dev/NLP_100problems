def head(data: list, n: str):
    for i in range(n):
        if data[i][-1] == "\n":
            print(data[i], end="")
        else:
            print(data[i])

def main():
    with open("./popular-names.txt", "r") as f:
        data = f.readlines()
    
    head(data, 5)

if __name__ == "__main__":
    main()