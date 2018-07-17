#MScoco2014のうちキャプションの単語とテキストが類似する画像を抽出し、保存するやつ
import numpy as np
import matplotlib
from typing import Any
from gensim.models import word2vec, Word2Vec
import sys
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
#import keyedvectors

matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from pycocotools.coco import COCO
import skimage.io as io
import coco_text

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def max_similar(ls1,ls2):
    for text1 in ls1:
        for text2 in ls2:
                if WordEmbeddingsKeyedVectors.vocab
                list.append(cos_sim(model[text1],model[text2]))
    return max(list)

def show(imgIds):
    img = ct.loadImgs(imgIds)[0]
    I = io.imread('%s/images/%s/%s' % (dataDir, dataType, img['file_name']))
    plt.axis('off')
    plt.imshow(I)
    plt.show()

def word_mat(imgIds):
    LS = []
    for img in imgIds:
        # load and display text annotations
        annIds = ct.getAnnIds(imgIds=img)
        anns = ct.loadAnns(annIds)
        ls=[]
        stop=len(anns)
        i = 0
        while i < stop:
            if ('utf8_string' in anns[i].keys()) == True:
                ls.append(anns[i]['utf8_string'])
            i += 1
        LS.append(ls)
    return LS

def cap_mat(imgIds):
    # initialize COCO api for caption annotations
    annFile_caption = '{}/annotations/train_val_annotation2014/captions_{}.json'.format(dataDir, dataType)
    coco_caps = COCO(annFile_caption)
    # load and display caption annotations
    annIds = coco_caps.getAnnIds(imgIds=imgIds)
    anns = coco_caps.loadAnns(annIds)
    ls=[]
    i=0
    stop = len(anns)
    while i < stop:
        ls.append(anns[i]['caption'])
        i += 1
    return ls

def wakati(caption):
    stop_words = nltk.corpus.stopwords.words('english')
    symbol = ["'", '"', ':', ';', '.', ',', '-', '!', '?', "'s"]
    stop_words += symbol
    words = word_tokenize(caption)
    wordsFiltered = []
    for w in words:
        if w not in stop_words:
            wordsFiltered.append(w)
    return wordsFiltered







dataDir='.'
dataType='train2014'
annFile_instance='{}/annotations/train_val_annotation2014/instances_{}.json'.format(dataDir,dataType)
ct = coco_text.COCO_Text('COCO_Text.json')
# initialize COCO api for instance annotations
coco=COCO(annFile_instance)
imgIds = ct.getImgIds(imgIds=ct.train,
                    catIds=[('legibility','legible')])

LS = word_mat(imgIds)
ls1 = LS[2]
ls2 = wakati(" ".join(cap_mat(imgIds[2])))
model = word2vec.Word2Vec.load("sample2.model")
print(max_similar(ls1,ls2))

show(imgIds[2])



