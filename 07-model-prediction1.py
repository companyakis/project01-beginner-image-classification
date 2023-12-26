#prediction 

X_head_five = X_test[:5]

y_predict_probability = model.predict(X_head_five)

#print(y_predict_probability)

#we should round values

print(y_predict_probability.round(2))
