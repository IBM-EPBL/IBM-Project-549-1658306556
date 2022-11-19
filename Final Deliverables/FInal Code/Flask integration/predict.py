import tensorflow as tf
#import load_model from keras.model
from keras.models import load_model
#import image class from keras
from keras.preprocessing import image
#import numpy
import numpy as np
#import cv2
import cv2

#Load the saved model
model = load_model("vgg19.h5")

#give any random image path
path = "E:/ds/dataset/test_set/FIRE/00923.jpg"
img = image.image_utils.load_img(path)
size = (224,224)
ds_img = tf.image.resize(img, size)
x = image.image_utils.img_to_array(ds_img)

#expand the image shape
x = np.expand_dims(x, axis= 0)
pred = model.predict(x)
pred = np.argmax(pred)
print(pred)