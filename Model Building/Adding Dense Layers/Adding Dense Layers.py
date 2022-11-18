#add hidden Layer
model.add(Dense(output_dim=150,init='uniform', activation='relu'))
#add output Layer
model.add(Dense (output_dim=1, activation='sigmoid', init='uniform'))
