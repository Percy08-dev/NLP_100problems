import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    header = tuple(map(lambda x:x.strip(), "ID \t TITLE \t URL \t PUBLISHER \t CATEGORY \t STORY \t HOSTNAME \t TIMESTAMP".split("\t")))
    df = pd.read_csv("./NewsAggregatorDataset/newsCorpora.csv", encoding="utf-8", delimiter="\t", names=header)
    publisher = {"Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"}
    
    df  = df[df["PUBLISHER"].isin(publisher)]
    
    train, test = train_test_split(df, test_size=0.2, train_size=0.8, random_state=42, shuffle=False)
    test, validation = train_test_split(test, test_size=0.5, train_size=0.5, random_state=42, shuffle=False)

    # print(len(train))
    # print(len(test))
    # print(len(validation))

    df.to_csv("all.tsv", sep="\t", encoding="utf-8", index=False)
    train.to_csv("./train.tsv", sep="\t", encoding="utf-8", index=False)
    test.to_csv("./test.tsv", sep="\t", encoding="utf-8", index=False)
    validation.to_csv("./validation.tsv", sep="\t", encoding="utf-8", index=False)




if __name__ == "__main__":
    main()