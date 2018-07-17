import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import coco_text

ct = coco_text.COCO_Text('COCO_Text.json')
pylab.rcParams['figure.figsize'] = (10.0, 8.0)

dataDir='.'
dataType='train2014'

# get all images containing at least one instance of legible text
imgIds = ct.getImgIds(imgIds=ct.train,
                    catIds=[('legibility','legible')])
# pick one at random
img = ct.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]


I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
print ('/images/%s/%s'%(dataType,img['file_name']))
plt.figure()
plt.imshow(I)
annIds = ct.getAnnIds(imgIds=img['id'])
anns = ct.loadAnns(annIds)
ct.showAnns(anns)
plt.show()

# load and display text annotations





def show(imgIds):
    img = ct.loadImgs(imgIds)[0]
    I = io.imread('%s/images/%s/%s' % (dataDir, dataType, img['file_name']))
    plt.axis('off')
    plt.imshow(I)


