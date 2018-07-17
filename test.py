from gensim.models import word2vec
import logging
import sys
import numpy as np


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def max_similar(ls1,ls2):
    #This function requiers numpy and cos_sim(the function to calculate cosine similarity).
    list = []
    len2 = len(ls2)
    for text1 in ls1:
        for text2 in ls2:
            list.append(cos_sim(model[text1],model[text2]))
    maxindex1 = (list.index(max(list))) // len2
    maxindex2 = (list.index(max(list))) % len2
    print(ls1[maxindex1],ls2[maxindex2])
    return max(list)

if __name__ == '__main__':
    # 学習済みモデルのロード
    model = word2vec.Word2Vec.load("sample2.model")
    ls1 = ["pose", "school", "love", "apple"]
    ls2 = ["college", "sea", "avenue"]
    print(max_similar(ls1, ls2))