#MScoco2014のうち情景内に文字を含む画像からランダムに一つ画像を抽出し、画像とテキストとキャプションを表示するやつ
import numpy as np
import matplotlib
from typing import Any

matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from pycocotools.coco import COCO
import skimage.io as io
import coco_text


#pylab.rcParams['figure.figsize'] = (8.0, 10.0)


dataDir='.'
dataType='train2014'
annFile_instance='{}/annotations/train_val_annotation2014/instances_{}.json'.format(dataDir,dataType)
ct = coco_text.COCO_Text('COCO_Text.json')


# initialize COCO api for instance annotations
coco=COCO(annFile_instance)

# display COCO categories and supercategories
# cats = coco.loadCats(coco.getCatIds())
# nms=[cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))
#
# nms = set([cat['supercategory'] for cat in cats])
# print('COCO supercategories: \n{}'.format(' '.join(nms)))

# きゃぷしょんにバスを含む画像のidsを取得
# catIds = coco.getCatIds(catNms=['bus'])
# imgIds = coco.getImgIds(imgIds=ct.train,
#                     catIds=catIds)

#画像内にテキストを少なくともひとつ含むもののidsを取得
imgIds = ct.getImgIds(imgIds=ct.train,
                    catIds=[('legibility','legible')])

#imgIds = coco.getImgIds(imgIds = [324158])
img = ct.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]


# 以下画像のロード、表示

I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))

plt.axis('off')
plt.imshow(I)

# initialize COCO api for caption annotations
annFile_caption = '{}/annotations/train_val_annotation2014/captions_{}.json'.format(dataDir,dataType)
coco_caps=COCO(annFile_caption)

# load and display caption annotations
annIds = coco_caps.getAnnIds(imgIds=img['id'])
anns = coco_caps.loadAnns(annIds)
print (anns[0]['caption'])
print (img)
coco_caps.showAnns(anns)

caption = anns[0]['caption']


# load and display text annotations
print("aaaaaa")
print(imgIds)
print(img["id"])
annIds = ct.getAnnIds(imgIds=img['id'])
anns = ct.loadAnns(annIds)

stop=len(anns)
i = 0
while i < stop:
    if ('utf8_string' in anns[i].keys()) == True:
        print('----------')
        print(anns[i]['utf8_string'])
        print('----------')
    i += 1





our_results = ct.loadRes('our_results.json')

ct.showAnns(anns)

plt.show()