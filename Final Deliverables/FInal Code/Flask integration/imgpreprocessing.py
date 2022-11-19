import keras  
from keras.preprocessing.image import ImageDataGenerator
def getdata():
    train_datagen = ImageDataGenerator (rescale=1./255,
                                        shear_range=0.2,
                                        rotation_range=180,
                                        zoom_range=0.2,
                                        horizontal_flip=True)

    test_datagen = ImageDataGenerator (rescale=1./255)
    val_datagen = ImageDataGenerator(rescale = 1./255)

    test_path = "E://ds//dataset//test_set"

    train_path = "E://ds//dataset//train_set"

    x_train = train_datagen.flow_from_directory(train_path, 
                                                target_size = (224,224), 
                                                batch_size = 32, 
                                                class_mode= 'binary')

    x_test = test_datagen.flow_from_directory(test_path, 
                                                target_size = (224,224), 
                                                batch_size = 32, 
                                                class_mode= 'binary')
    val_set = val_datagen.flow_from_directory(test_path,
                                            target_size = (224, 224),
                                            batch_size = 32,
                                            class_mode = 'binary')
    return x_train, x_test, val_set
