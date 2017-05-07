#s3132392 Casey-Ann Charlesworth
#Assignment 2 - Practical Data Science
#Assignment due 18 May 2017


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

files = ["red", "white"]
var = ["fixed acidity","volatile acidity","citric acid","residual sugar",
       "chlorides","free sulfur dioxide","total sulfur dioxide","density",
       "pH","sulphates","alcohol"]
class_var = ["quality"]
target_names = ['3','4','5','6','7','8']
k = 100


#import file and create summary graphs
for f in files:
    filename = f + ".csv"
    wineq = pd.read_csv(filename,sep=",",header=0)

    #K nearest neighbours
    y = wineq.quality.values
    X = wineq[var].values
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=0)
    clf = KNeighborsClassifier(k)
    fit = clf.fit(X_train,y_train)
    predicted = fit.predict(X_test)
    cm = confusion_matrix(y_test, predicted)
    cr = classification_report(y_test, predicted)

    #Calculate confusion error rate
    cer = accuracy_score(y_test, predicted)
    
    #Print confusion matrix
    plt.imshow(cm, cmap=plt.cm.Purples)
    plt.title("KNN confusion matrix: " + f + " wine (k=" + str(k) + ")\n Classification error rate = " + str(round(cer,3)))
    
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.colorbar()
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names)
    plt.yticks(tick_marks, target_names)
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.show()

    #Print classification report (to screen)
    print(cr)


print("Modelling complete")
