#Define the parameters /arguments for ImageDataGenerator class
train_datagen=ImageDataGenerator (rescale=1./255,
shear_range=0.2,
rotation_range=180,
zoom_range=0.2,
horizontal_flip=True)
test_datagen=ImageDataGenerator (rescale=1./255)
