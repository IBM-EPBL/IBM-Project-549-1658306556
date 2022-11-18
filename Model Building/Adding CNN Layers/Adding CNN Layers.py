#add convolutional Layer
model.add(Convolution2D(32, (3,3),input_shape=(128,128,3), activation='relu'))
#add maxpooling Layer
model.add(MaxPooling2D(pool_size=(2,2)))
#add flatten Layer
model.add(Flatten())
