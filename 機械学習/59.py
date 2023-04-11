import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from scipy.sparse import spmatrix, csr_matrix, load_npz
import matplotlib.pyplot as plt
import tqdm
import numpy as np
import optuna



class Model:
    def __init__(self, train_x, train_y, validation_x, validation_y) -> None:
        self.train_x = train_x
        self.train_y = train_y
        self.validation_x = validation_x
        self.validation_y = validation_y

    def __call__(self, trial):
        params = {
            'solver' : trial.suggest_categorical('solver', ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']),
            'C': trial.suggest_loguniform('C', 0.0001, 10),
            'max_iter': trial.suggest_int('max_iter', 100, 100000),
            'random_state':42
        }
        lg = LogisticRegression(**params)
        lg.fit(self.train_x, self.train_y)
        pred = lg.predict(self.validation_x)
        ac = accuracy_score(pred, self.validation_y)
        return ac


def main():
    # 特徴量
    train_feature = load_npz("./train.feature.npz")
    test_feature = load_npz("./test.feature.npz")
    validation_feature = load_npz("./validation.feature.npz")

    # データロード
    train = pd.read_csv("./train.tsv", encoding="utf-8", sep="\t")
    test =  pd.read_csv("./test.tsv", encoding="utf-8", sep="\t")
    validation =  pd.read_csv("./validation.tsv", encoding="utf-8", sep="\t")
    
    # 最適化
    obj = Model(train_x=train_feature, train_y=train["CATEGORY"], validation_x=validation_feature, validation_y=validation["CATEGORY"])
    study = optuna.create_study(direction='maximize')
    study.optimize(obj, timeout=60, n_jobs=-1)

    print('params:', study.best_params)

    # 最適化後のスコア
    lg = LogisticRegression(**study.best_params)
    lg.fit(train_feature, train["CATEGORY"])

    pred_train = lg.predict(train_feature)
    pred_test = lg.predict(test_feature)

    ac_train = accuracy_score(train["CATEGORY"], pred_train)
    ac_test = accuracy_score(test["CATEGORY"], pred_test)

    print("　学習データ正解率:{}".format(ac_train))
    print("テストデータ正解率:{}".format(ac_test))


if __name__ == "__main__":
    main()
