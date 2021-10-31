def main():
    with open("./popular-names.txt", "r") as f:
        data = f.readlines()

    col1 = [i.split()[0] + "\n" for i in data]
    col2 = [i.split()[1] + "\n" for i in data]
    
    with open("./col1.txt", "w", newline="\n") as f:
        f.writelines(col1)

    with open("./col2.txt", "w", newline="\n") as f:
        f.writelines(col2)

if __name__ == "__main__":
    main()