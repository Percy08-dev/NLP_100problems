def main():
    with open("./popular-names.txt", "r") as f:
        data = f.readlines()
    
    data = [i.replace("\t", " ") for i in data]
    

    with open("./out.txt", "w", newline="\n") as f:
        f.writelines(data)

if __name__ == "__main__":
    main()