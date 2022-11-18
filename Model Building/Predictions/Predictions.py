#import load_model from keras.model
from keras.models import load_model
#import image class from keras
from keras.preprocessing import image
#import numpy
import numpy as np
#import cv2
import cv2
#Load the saved model
model = load_model("forest1.h5")
#give any random image path
img image.load_img(r'D:\Artificial Intelligence with Flask\ Forest Combustion Recognition using AI\Main Pi =
X = image.img_to_array(img)
#expand the image shape
x = np.expand_dims (x, axis= 0)
pred = model.predict_classes(x)
