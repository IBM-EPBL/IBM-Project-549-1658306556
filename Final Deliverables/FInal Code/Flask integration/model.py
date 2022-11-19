#To define linear intialisation import Sequential 
from keras.models import Sequential
#To add Layers import Dense
from keras.layers import Dense
#To create Convolution kernel import convolution2D
from keras.layers import Convolution2D
#import Maxpooling layer
from keras.layers import MaxPooling2D
#import Flatten Layer
from keras.layers import Flatten
import warnings
warnings.filterwarnings('ignore')

from imgpreprocessing import getdata

x_train, x_test = getdata()

#intializing the model 
model = Sequential()
#add convolutional Layer 
model.add(Convolution2D(32, (3,3),input_shape=(128,128,3), activation='relu'))
#add maxpooling Layer 
model.add(MaxPooling2D(pool_size=(2,2)))
#add convolutional Layer 
model.add(Convolution2D(32, (3,3),input_shape=(128,128,3), activation='relu'))
#add maxpooling Layer 
model.add(MaxPooling2D(pool_size=(2,2)))
#add convolutional Layer 
model.add(Convolution2D(32, (3,3),input_shape=(128,128,3), activation='relu'))
#add maxpooling Layer 
model.add(MaxPooling2D(pool_size=(2,2)))

#add flatten Layer 
model.add(Flatten())

#add hidden Layer 
model.add(Dense(32,activation='relu'))
#add hidden Layer 
model.add(Dense(64,activation='relu'))
#add hidden Layer 
model.add(Dense(128,activation='relu'))

#add output layer
model.add(Dense(1,activation='softmax'))

model.compile(loss= 'binary_crossentropy',
                optimizer= 'adam',
                metrics= ["accuracy"])

#Training the model 
model.fit_generator(x_train, steps_per_epoch=14, 
                    epochs=30, validation_data=x_test, 
                    validation_steps=85)

#save the model
model.save("vgg19.h5")

import visualkeras

visualkeras.layered_view(model).show() # display using your system viewer
visualkeras.layered_view(model, to_file='output.png') # write to disk
visualkeras.layered_view(model, to_file='output.png').show() # write and show

visualkeras.layered_view(model)