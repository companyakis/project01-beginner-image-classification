# data preprocessing

# split data (train and test data)

(X_train_all, y_train_all), (X_test, y_test) = fashion_mnist_data

#print(X_train_all.shape)
#print(y_train_all.shape)
#print(X_test.shape)
#print(y_test.shape)

# Train, validation and test data

# 55000 train and 5000 validation data

X_train = X_train_all[:55000]
y_train = y_train_all[:55000]

#print(X_train.shape)
#print(y_train.shape)

X_validation = X_train_all[-5000:]
y_validation = y_train_all[-5000:]

#print(X_validation.shape)
#print(y_validation.shape)

#look data
#print(X_train[0])
#print(X_train.dtype) #uint8

X_train, X_validation, X_test = X_train/255.0, X_validation/255.0, X_test/255.0

#look data again
#print(X_train[0])
#print(X_train.dtype) #float64

#what about y?
#print(y_train[0]) #9

#print(np.unique(y_train)) #[0 1 2 3 4 5 6 7 8 9]

#we should give class names

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal",  "Shirt", "Sneaker", "Bag", "Ankle boot"]
              

#remember y_train[0] is equal to 9

#print(class_names[y_train[0]]) #now not 9, Ankle boot
