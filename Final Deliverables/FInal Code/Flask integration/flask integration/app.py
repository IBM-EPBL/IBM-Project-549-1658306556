from flask_sqlalchemy import SQLAlchemy
import tensorflow as tf
#import load_model from keras.model
from keras.models import load_model
#import image class from keras
from keras.preprocessing import image
from flask import Flask, redirect, render_template, Response, request, url_for
import cv2
import numpy as np
from twilio.rest import Client
from playsound import playsound


#Load the saved model
model = load_model("C:/Users/mithun/Desktop/ibm-project-main/vgg19.h5")

global rec_frame, switch, rec, p
capture=0
switch=1
rec=1


#instatiate flask app  
app = Flask(__name__,template_folder='./templates')
app.config['threaded'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))


camera = cv2.VideoCapture(0)

def predict(img):
    size = (224,224)
    img = tf.image.resize(img, size)
    x = image.image_utils.img_to_array(img)

    #expand the image shape
    x = np.expand_dims(x, axis= 0)
    pred = model.predict(x)
    pred = np.argmax(pred)
    print(pred)
    if pred == 1:
        p = "no fire"
        
    else:
        p = "fire"
        # #twilio account ssid
        # account_sid = 'AC47e7689f6c300dd7c3a89dad1deefffb'
        # #twilio account authentication token
        # auth_token= '909b27f853acccdddcf1983334625421'

        # client = Client(account_sid, auth_token)
        # message = client.messages \
        #                 .create(
        #                     body="Forest fire is detected. Stay alert.",
        #                     from_='+15737702572',
        #                     to='+917010461435'
        #                 )
        # print(message.sid)
        # print("Fire Detected")
        # print("SMS sent!")
        # a = "C://Users//mithun//Desktop//ibm-project-main//siren.mp3"
        # playsound(a, True)    
    return p

def gen_frames():  # generate frame by frame from camera
    global out, capture,rec_frame
    while True:
        success, frame = camera.read() 
        if success:          
            if(rec):
                rec_frame=frame
                p = predict(rec_frame)
                frame = cv2.putText(cv2.flip(frame,1),p, (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),4)
                frame = cv2.flip(frame,1)  
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass


@app.route('/')
def index():
    return render_template('home.html')
    
@app.route("/login",methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("cam_feed"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout",methods=["POST","GET"])
def logout():
    switch=0
    rec=0
    camera.release()
    # cv2.destroyAllWindows()
    return render_template("logout.html")

@app.route("/cam_feed",methods=["POST","GET"])
def cam_feed():
    if request.method == "POST":
        return redirect(url_for('logout'))
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/requests',methods=['POST','GET'])
def tasks():
    global switch,camera
    if request.method == 'POST':
        if  request.form.get('stop') == 'Stop/Start':
            
            if(switch==1):
                switch=0
                rec=0
                camera.release()
                cv2.destroyAllWindows()
                
            else:
                camera = cv2.VideoCapture(0)
                switch=1
                rec=1
                          
                 
    elif request.method=='GET':
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
    
camera.release()
cv2.destroyAllWindows()     