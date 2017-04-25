import cv2
import numpy as np
import glob
import os
folders = os.listdir("train")
counter = 0
home = "/home/ubuntu/train/"
for folder in folders:
	train_data = [img for img in glob.glob(home+folder+"/*jpg")]
	print folder
	for index,image_path in enumerate(train_data):
		image = cv2.imread(image_path)
		(h, w) = image.shape[:2]
		center = (w / 2, h / 2)
 		for i in range(1,361, 10):
			M = cv2.getRotationMatrix2D(center, i, 1.0)
			rotated = cv2.warpAffine(image, M, (w, h))
			img = image_path.replace(".jpg", str(i)+".jpg")
			cv2.imwrite(img, rotated)
			counter = counter + 1
	print counter

