#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import numpy as np
#from gensim.models import word2vec
from gensim.models import KeyedVectors

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# 学習済みモデルのロード
#model = word2vec.Word2Vec.load("sample2.model")
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)




for ids=1








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

# 入力された単語から近い単語をn個表示する
def s(posi, nega=[], n=100):
    cnt = 1  # 表示した単語の個数カウント用
    # 学習済みモデルからcos距離が最も近い単語n個(topn個)を表示する
    result = model.most_similar(positive=posi, topn=n)
    for r in result:
        print(cnt, '　', r[0], '　', r[1])
        cnt += 1

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


if __name__ == '__main__':
    print(cos_sim(model["taxi"], model["bus"]))
    s(posi = ["taxi"])