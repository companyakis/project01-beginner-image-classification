#The numpy.argmax() function returns indices of the max element of the array in a particular axis

y_prediction = y_predict_probability.argmax(axis = -1)

print(y_prediction) #[9 2 1 1 6]

print(np.array(class_names)[y_prediction]) #['Ankle boot' 'Pullover' 'Trouser' 'Trouser' 'Shirt']
