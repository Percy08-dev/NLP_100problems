import gensim
import numpy as np
import pandas as pd
import torch
import tqdm


def feature_and_collect(df:pd.DataFrame, model:gensim.models.KeyedVectors):
    table = {'b': 0, 't': 1, 'e':2, 'm':3}
    text = df["TITLE"]
    ans = [table[i] for i in df["CATEGORY"]]
    text_vecs = list()

    for row in tqdm.tqdm(text):
        vec = [model[word] for word in row.split(" ") if word in model]
        if len(vec) > 0:
            text_vecs.append(sum(vec)/len(vec))
        else:
            text_vecs.append(np.zeros(300))

    return torch.tensor(text_vecs), torch.tensor(ans)



def main():
    df = pd.read_csv("../機械学習/all.tsv", sep="\t", encoding="utf-8")
    model = gensim.models.KeyedVectors.load_word2vec_format("./GoogleNews-vectors-negative300.bin.gz", binary=True)

    feature_and_collect(df, model)



if __name__ == "__main__":
    main()
