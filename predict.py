import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import glob

  
    # You can use the commented block of code below to
    #  make sure that caffe is on the python path:
    # This takes the path to caffe_root from the environment variable, so make sure
    # the $CAFFE_ROOT environment variable is set
    #
    #
#caffe_root = os.environ['/home/ubuntu/caffe/']
#import sys
#sys.path.insert(0, caffe_root + 'python')
   

import caffe

   
    # Adapted from from : http://www.cc.gatech.edu/~zk15/deep_learning/classify_test.py
   

    # Set the right path to your model definition file, pretrained model weights,
    # and the image you would like to classify.   
MODEL_FILE = '/home/kunwar/deep-learning/that_worked/deploy.prototxt'
PRETRAINED = '/home/kunwar/deep-learning/that_worked/snapshots_2500.caffemodel'
BINARY_PROTO_MEAN_FILE = "/home/kunwar/deep-learning/that_worked/mean.binaryproto"

   
    # Replicated from https://github.com/BVLC/caffe/issues/290
   
blob = caffe.proto.caffe_pb2.BlobProto()
data = open( BINARY_PROTO_MEAN_FILE  , 'rb' ).read()
blob.ParseFromString(data)
mean_arr = np.array( caffe.io.blobproto_to_array(blob) )[0]


    ##NOTE : If you do not have a GPU, you can uncomment the `set_mode_cpu()` call
    #        instead of the `set_mode_gpu` call.
#caffe.set_mode_gpu()
caffe.set_mode_cpu()


net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=mean_arr.mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(227, 227))

f = open("output_probability.csv", "w")

number_of_files_processed = 0
for _file in glob.glob("testdata/*jpg"):
         number_of_files_processed += 1
         FileName = _file.split("/")[-1]
         input_image = caffe.io.load_image(_file)
         prediction = net.predict([input_image])
         s = FileName+","+ prediction[0].argmax()+","
         for probability in prediction[0]:
             s+=str(probability)+","
         s = s[:-1]+"\n"
         f.write(s)
         print "Number of files : ", number_of_files_processed
         print 'predicted class:', prediction[0].argmax()
         print "**********************************************"
