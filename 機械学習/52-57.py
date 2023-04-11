import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from scipy.sparse import spmatrix, csr_matrix, load_npz
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

    # 学習
    lg = LogisticRegression(random_state=42, max_iter=10000)
    lg.fit(train_feature, train["CATEGORY"])

    # 予測
    pred_train = lg.predict(train_feature)
    pred_test = lg.predict(test_feature)
    
    # 学習データ
    print("TrainData")
    print(confusion_matrix(pred_train, train["CATEGORY"]))
    print(classification_report(pred_train, train["CATEGORY"]))

    # テストデータ
    print("TestData")
    print(confusion_matrix(pred_test, test["CATEGORY"]))
    print(classification_report(pred_test, test["CATEGORY"]))

    # 重み
    features = pd.read_csv("./feature_names.csv", encoding="utf-8")

    # 重み上位の出力
    for c, coef in zip(lg.classes_, lg.coef_):
        print(f'【カテゴリ】{c}')
        # 行番号で指定して抽出した後に、行と列の名前を変更
        best10 = features.iloc[np.argsort(coef)[::-1][:10]].rename(columns={"0": '重要度上位'}, index={n:i for i, n in enumerate(np.argsort(coef)[::-1][:10], start=1)}).T
        worst10 = features.iloc[np.argsort(coef)[:10]].rename(columns={"0": '重要度下位'}, index={n:i for i, n in enumerate(np.argsort(coef)[:10], start=1)}).T
        print(pd.concat([best10, worst10], axis=0))
        print('\n')

    # ハイパーパラメータの調整



if __name__ == "__main__":
    main()

