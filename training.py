
import pandas as pd 
from collections import defaultdict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix
import keras
from keras.models import Sequential
from keras.layers import Dense
import model
import random
from keras.utils.vis_utils import plot_model


n_dim=10
epochs=250
batch_size=64
output_dim=5

isTrain=True
# df[df==np.inf]=np.nan
# df.fillna(df.mean(), inplace=True)
df_train=pd.read_csv("clean_data.csv")
list_num=[x for x in df_train.columns if x not in ['label','general','Unnamed: 0']]
cate_dict={'__label__18-24':0,'__label__45-54':3, '__label__25-34':1,'__label__35-44':2,'__label__55+':4}
pca = PCA(n_components=n_dim)
ohe = OneHotEncoder()

def drop_row(df,list_num=list_num,num_group=2):
    new_df=df
    count=0
    for index,row in df[list_num].iterrows():
        
        if(row.sum()<=num_group):
            new_df=new_df.drop(index)
            count+=1
    return new_df
def drop_row_1(df,list_num=list_num,num_group=0):
    new_df=df
    count=0
    f=open("index.txt","w")
    
    for index,row in df[list_num].iterrows():
        
        if(row.sum()<=num_group):
            f.write(str(index)+"\n")
    f.close()
    return df
def preprocess(df,list_num=list_num,num_group=2, isDropRow=True):
    if isDropRow:
        df =drop_row(df)
    else: df=drop_row_1(df)
    df[list_num]=df[list_num].div(df[list_num].sum(axis=1),axis=0)
    return df


def OneHot(y):
    y=np.array(y).reshape(-1,1)
    return ohe.fit_transform(y).toarray()

df_train=preprocess(df_train,isDropRow=True)
df_train['label']=df_train['label'].replace(cate_dict)
y=df_train['label'].values

X_train=np.array(df_train[list_num].values)
pca.fit(X_train)

if isTrain:
    # y_train = OneHot(y)
    X_train=pca.transform(X_train)
    y_train=OneHot(y)

    ANN=model.NeuralModel([16,32,64,128,64,32,16], input_dim=n_dim, output_dim=output_dim)
    history = ANN.fit(X_train, y_train, epochs=epochs, batch_size=64)
    # ANN = model.KNN(n_neighbors=100)
    # ANN.fit(X_train,y)
    # ANN=model.SVM(kernel="rbf")
    # ANN.fit(X_train,y)
else :
    ANN=model.loadNeuralModel()

df_test=pd.read_csv("data_0_1000.csv")

df_test=preprocess(df_test,isDropRow=False)

X_test = df_test[list_num]
df_test['label']=df_test['label'].replace(cate_dict)
y_test = df_test['label'].values


y_test=OneHot(y_test)
# y_test=np.array(y_test).reshape(-1,1)
# print(X_test.describe())
X_test=np.nan_to_num(X_test.values)
X_test=pca.transform(X_test)

y_pred = ANN.predict(X_test)

print(model.calcAccuracy(y_pred,y_test,isOneHot=True))

y_pred = [np.argmax(i) for i in y_pred]
y_test = [np.argmax(i) for i in y_test]
print(confusion_matrix(y_test,y_pred,labels=[0,1,2,3,4]))
model.saveNeuralModel(ANN)

df_test=pd.read_csv("total_data_test.csv")

df_test=preprocess(df_test,isDropRow=False)

X_test = df_test[list_num]
# df_test['label']=df_test['label'].replace(cate_dict)
# y_test = df_test['label'].values


# y_test=OneHot(y_test)
# y_test=np.array(y_test).reshape(-1,1)
# print(X_test.describe())
X_test=np.nan_to_num(X_test.values)
X_test=pca.transform(X_test)

y_pred = ANN.predict(X_test)

# print(model.calcAccuracy(y_pred,y_test,isOneHot=True))

y_pred = [np.argmax(i) for index,i in enumerate(y_pred) ]
f=open("_result.txt","w")
for index,i in enumerate(y_pred) :
    for name,age in cate_dict.items():
        
        if age==i:
            f.write(name+"\n")
f.close()
