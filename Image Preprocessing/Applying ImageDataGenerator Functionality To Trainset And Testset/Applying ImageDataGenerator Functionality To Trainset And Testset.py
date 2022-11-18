# Applying ImageDataGenerator functionality to trainset.
x_train = train_datagen.flow_from_directory(r'./Main Project/Dataset Main/train_set', target_size = (128,128), batch_size = 32, class_mode= 'binary')
# Applying ImageDataGenerator functionality to testset.
x_test = test_datagen.flow_from_directory(r'./Main Project/Dataset Main/test_set', target_size = (128,128), batch_size = 32, class_mode= 'binary')
