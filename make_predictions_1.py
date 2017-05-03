import os
import glob
import cv2
import caffe
import lmdb
import numpy as np
from caffe.proto import caffe_pb2

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
with open('/home/kunwar/deep-learning/that_worked/mean.binaryproto') as f:
    mean_blob.ParseFromString(f.read())
mean_array = np.asarray(mean_blob.data, dtype=np.float32).reshape(
    (mean_blob.channels, mean_blob.height, mean_blob.width))


#Read model architecture and trained model's weights
net = caffe.Net('/home/kunwar/deep-learning/that_worked/deploy.prototxt',
                '/home/kunwar/deep-learning/that_worked/snapshots_iter_2500.caffemodel',
                caffe.TEST)

#Define image transformers
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', mean_array)
transformer.set_transpose('data', (2,0,1))

'''
Making predictions
'''
#Reading image paths
test_img_paths = [img_path for img_path in glob.glob("/home/kunwar/deep-learning/that_worked/testdata/*jpg")]

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

    print img_path
    print pred_probas.argmax()
    print '-------'

'''
Making submission file
'''
with open("/home/kunwar/deep-learning/that_worked/output2.csv","w") as f:
    f.write("legends, Class1=0,Class2=11,Class3=22,Class4=33,Class5=39,Class6=36,Class7=37,Class8=38,Class9=39,Class10=1,Class11=2,Class12=3,Class13=4,Class14=5,Class15=6,Class16=7,Class17=8,Class18=9,Class19=10,Class20=12,Class21=13,Class22=14,Class23=15,Class24=16,Class25=17,Class26=18,Class27=19,Class28=20,Class29=21,Class30=23,Class31=24,Class32=25,Class33=26,Class34=27,Class35=28,Class36=29,Class37=30,Class38=31,Class39=32,Class40=34,Class41=35,Class42=36,Class43=37,Class44=38, \n")
    f.write("id, predicted label, predicted name\n")
    for i in range(len(test_ids)):
        f.write(str(test_ids[i])+","+str(preds[i])+","+str(mydict[preds[i]])+"\n")
f.close()
