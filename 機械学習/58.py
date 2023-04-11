import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from scipy.sparse import spmatrix, csr_matrix, load_npz
import matplotlib.pyplot as plt
import tqdm
import numpy as np


def main():
    # 特徴量
    train_feature = load_npz("./train.feature.npz")
    test_feature = load_npz("./test.feature.npz")
    validation_feature = load_npz("./validation.feature.npz")

    # データロード
    train = pd.read_csv("./train.tsv", encoding="utf-8", sep="\t")
    test =  pd.read_csv("./test.tsv", encoding="utf-8", sep="\t")
    validation =  pd.read_csv("./validation.tsv", encoding="utf-8", sep="\t")

    # 正則化パラメータの調整
    list_ac_train = list()
    list_ac_test = list()
    x = list()
    for c in tqdm.tqdm(np.logspace(-10, 10, num=20, base=10)):
        x.append(c)
        # 学習
        lg = LogisticRegression(random_state=42, max_iter=10000, C=c)
        lg.fit(train_feature, train["CATEGORY"])
        # 予測
        pred_train = lg.predict(train_feature)
        pred_test = lg.predict(test_feature)
        # 正解率
        ac_train = accuracy_score(train["CATEGORY"], pred_train)
        list_ac_train.append(ac_train)
        ac_test = accuracy_score(test["CATEGORY"], pred_test)
        list_ac_test.append(ac_test)

    # 描写
    plt.plot(x, list_ac_train, label="Train")
    plt.plot(x, list_ac_test, label="Test")
    plt.ylim(0, 1.1)
    plt.ylabel('Accuracy')
    plt.xscale ('log')
    plt.xlabel('C')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()