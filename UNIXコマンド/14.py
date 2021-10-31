from typing import TextIO

def head(f:TextIO, n: str):
    for row, _ in zip(f, range(n)):
        print(row, end = "")

def main():
    with open("./popular-names.txt", "r") as f:
        head(f, 10)

if __name__ == "__main__":
    main()