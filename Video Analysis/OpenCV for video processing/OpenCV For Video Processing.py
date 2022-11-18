#import opencv library
import cv2
#import numpy
import numpy as np
#import image function from keras
from keras.preprocessing import image
#import load_model from keras
from keras.models import load_model
#import Client from twilio API
from twilio.rest import Client
#import playsound package
from playsound import playsound

#load the saved model
model = load_model(r' forest1.h5')
#define video
video = cv2.VideoCapture(0)
#define the featues
name = ['forest', 'with fire']
