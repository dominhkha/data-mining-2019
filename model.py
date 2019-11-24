import keras
from keras.models import Sequential,model_from_json
from keras.layers import Dense,Dropout
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np 

def NeuralModel(layers,input_dim, output_dim,activation='relu'):
    model = Sequential()
    for layer in layers:
        if(layer<1):
            model.add(Dropout(layer))
            continue
        model.add(Dense(layer,activation = activation))
    model.add(Dense(output_dim,activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        
    return model;
def saveNeuralModel(model):
    with open("_model.json","w") as json_file:
        model_json=model.to_json()
        json_file.write(model_json)
    model.save_weights("_weights.h5")

def loadNeuralModel():
    json_file=open("_model.json","r")
    loaded_model = model_from_json(json_file.read())
    json_file.close()
    loaded_model.load_weights("_weights.h5")
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return loaded_model
def KNN(n_neighbors, weights="distance"):
    return KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights)

def SVM(kernel="linear",gamma='scale'):
    return svm.SVC(gamma=gamma,kernel=kernel,verbose=False, C=1)


def calcAccuracy(y_pred,y_test,isOneHot=True):
    pred = y_pred
    test = y_test
    if isOneHot:
        pred = [np.argmax(i) for i in y_pred]
        test = [np.argmax(i) for i in y_test]
    return accuracy_score(pred,test)


def count_label(df, column='label'):
    return df[column].value_counts().to_dict()
