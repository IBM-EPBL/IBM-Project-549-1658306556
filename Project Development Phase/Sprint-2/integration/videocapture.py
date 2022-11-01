#import opencv library
from importlib.resources import path
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
model = load_model('vgg19.h5')
#define video
video = cv2.VideoCapture(0)
#define the featues
name = ('FIRE', 'NON_FIRE')
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (600,600)
fontScale              = 2
fontColor              = (255,165,0)
thickness              = 2
lineType               = 2

while(1):
    success, frame = video.read()
    cv2.imwrite("image.jpg", frame)
    img = image.image_utils.load_img("image.jpg", target_size = (224,224))
    x = image.image_utils.img_to_array(img)
    x = np.expand_dims(x,axis= 0)
    pred = model.predict(x)
    pred = np.argmax(pred)
    p = pred
    if p == 1:
        q = "forest"
    else:
        q = "with fire"
    print(pred)
    frame = cv2.putText(cv2.flip(frame,1),q, (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),4)

    pred = model.predict(x)
    if p == 0:
        # #twilio account ssid
        # account_sid = 'AC47e7689f6c300dd7c3a89dad1deefffb'
        # #twilio account authentication token
        # auth_token= '909b27f853acccdddcf1983334625421'

        # client = Client (account_sid, auth_token)
        # message = client.messages \
        #                 .create(
        #                     body="Forest fire is detected. Stay alert.",
        #                     from_='+15737702572',
        #                     to='+917010461435'
        #                 )
        # print(message.sid)
        print("Fire Detected")
        print("SMS sent!")
        a = "C://Users//mithun//Desktop//ibm-project-main//tornado-siren.mp3"
        # playsound(a, True)

    else:
        print("No Danger")
    cv2.imshow("image",frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

video.release()
cv2.destroyAllWindows()
