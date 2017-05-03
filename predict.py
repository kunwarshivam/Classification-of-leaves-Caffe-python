import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
sys.path.append('/home/kunwar/deep-learning/caffe/python')
import os
import glob
import cv2
import lmdb
import caffe
import numpy as np
from caffe.proto import caffe_pb2
dictionary = {0:"Class1-cerris",	11:"Class2-purpubascens",	22:"Class3-hispanica",	33:"Class4-kewensis",	39:"Class5-ludoviciana",	40:"Class6-mannifera",	41:"Class7-rosacea",	42:"Class8-turneri",	43:"Class9-cutissima",	1:"Class10-agriefolia",	2:"Class11-agrifolia",	3:"Class12-arkansana",	4:"Class13-boissieri",	5:"Class14-canariensis", 6:"Class15-castaneifolia",	7:"Class16-cerris",	8:"Class17-ellipsoidalis",	9:"Class18-frainetto",	10:"Class19-hartwissiana",	12:"Class20-hemisphaerica",	13:"Class21-hybrid",	14:"Class22-ilex",	15:"Class23-infectoria",	16:"Class24-ithaburensis",	17:"Class25-laurifolia",	18:"Class26-lobata",	19:"Class27-macransmera",	20:"Class28-marilandica",	21:"Class29-oxyodon",	23:"Class30-petraea",	24:"Class31-petraer_fmespilikolia",	25:"Class32-phellos",	26:"Class33-pubescens",	27:"Class34-reticulata",	28:"Class35-rhysophylla",	29:"Class36-robur",	30:"Class37-rotundifolia",	31:"Class38-rubra",	32:"Class39-rulstra_aurea",	34:"Class40-serrata",	35:"Class41-shumardii",	36:"Class42-trotana",	37:"Class43-uercus",	38:"Class44-qvariabilis"
} 
filenames = ["Class1","Class2","Class3","Class4","Class5","Class6","Class7","Class8","Class9","Class10","Class11","Class12","Class13","Class14","Class15","Class16","Class17","Class18","Class19","Class20","Class21","Class22","Class23","Class24","Class25","Class26","Class27","Class28","Class29","Class30","Class31","Class32","Class33","Class34","Class35","Class36","Class37","Class38","Class39","Class40","Class41","Class42","Class43","Class44"]
filenames = sorted(filenames)
mydict={}
for index_label , folder_name in enumerate(filenames):
	      mydict[index_label] = folder_name

caffe.set_mode_cpu()

#Size of images
IMAGE_WIDTH = 227
IMAGE_HEIGHT = 227

'''
Image processing helper function
'''

def transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT):

    #Histogram Equalization
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])

    #Image Resizing
    img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_CUBIC)

    return img


'''
Reading mean image, caffe model and its weights
'''
#Read mean image
mean_blob = caffe_pb2.BlobProto()
with open('/var/www/html/project/mean.binaryproto') as f:
    mean_blob.ParseFromString(f.read())
mean_array = np.asarray(mean_blob.data, dtype=np.float32).reshape(
    (mean_blob.channels, mean_blob.height, mean_blob.width))


#Read model architecture and trained model's weights
net = caffe.Net('/var/www/html/project/deploy.prototxt',
                '/var/www/html/project/snapshots_iter_2500.caffemodel',
                caffe.TEST)

#Define image transformers
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', mean_array)
transformer.set_transpose('data', (2,0,1))

'''
Making predictions
'''
#Reading image paths
test_img_paths = [img_path for img_path in glob.glob("/var/www/html/project/abcd/*jpg")]

#Making predictions
test_ids = []
preds = []
for img_path in test_img_paths:
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img = transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)

    net.blobs['data'].data[...] = transformer.preprocess('data', img)
    out = net.forward()
    pred_probas = out['prob']

    test_ids = test_ids + [img_path.split('/')[-1][:-4]]
    preds = preds + [pred_probas.argmax()]

    print pred_probas.argmax()
    print dictionary[pred_probas.argmax()]
