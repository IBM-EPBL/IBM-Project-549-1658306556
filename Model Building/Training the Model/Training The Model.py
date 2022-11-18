#Training the model
model.fit_generator (x_train, steps_per_epoch=14, epochs=10, validation_data=x_test, validation_steps=4)
