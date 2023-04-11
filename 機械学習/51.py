import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import spmatrix, csr_matrix, save_npz
import numpy as np


# 分散表現の章が後にあるから、古典的な手法で
def feature(df:pd.DataFrame, V:TfidfVectorizer)->csr_matrix:
    return V.transform(df).tocsr()      # csr形式で圧縮


def main():
    train = pd.read_csv("./train.tsv", encoding="utf-8", sep="\t")
    test =  pd.read_csv("./test.tsv", encoding="utf-8", sep="\t")
    validation =  pd.read_csv("./validation.tsv", encoding="utf-8", sep="\t")
    
    V = TfidfVectorizer(min_df=0, max_df=1000)
    V.fit(train["TITLE"])               # Learn vocabulary and idf from training set.

    train_feature = feature(train["TITLE"], V)
    test_feature = feature(test["TITLE"], V)
    validation_feature = feature(validation["TITLE"], V)

    save_npz("./train.feature", train_feature)
    save_npz("./test.feature", test_feature)
    save_npz("./validation.feature", validation_feature)
    pd.DataFrame(V.get_feature_names_out()).to_csv("feature_names.csv", sep=",", index=False, encoding="utf-8")
    


if __name__ == "__main__":
    main()

