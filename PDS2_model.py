#s3132392 Casey-Ann Charlesworth
#Assignment 2 - Practical Data Science
#Assignment due 18 May 2017


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#Function to print confusion matrix
def print_confusion_matrix(cm, title, cer, color):
    plt.imshow(cm, cmap=color)
    plt.title(title)
    
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

#Define variables
files = ["red", "white"]
var = ["fixed acidity","volatile acidity","citric acid","residual sugar",
       "chlorides","free sulfur dioxide","total sulfur dioxide","density",
       "pH","sulphates","alcohol"]
class_var = ["quality"]


#import file and create summary graphs
for f in files:
    filename = f + ".csv"
    wineq = pd.read_csv(filename,sep=",",header=0)

    if f == "red":
        target_names = ['3','4','5','6','7','8']
    elif f == "white":
        target_names = ['3','4','5','6','7','8','9']

    #K nearest neighbours
    k = 1
    y = wineq.quality.values
    X = wineq[var].values
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=4)
    clf = KNeighborsClassifier(k)
    fit = clf.fit(X_train,y_train)
    predicted = fit.predict(X_test)
    cm = confusion_matrix(y_test, predicted)
    cr = classification_report(y_test, predicted)

    #Calculate confusion error rate
    acc = accuracy_score(y_test, predicted)
    cer = 1-acc
    
    #Print confusion matrix
    print_confusion_matrix(cm, title="KNN confusion matrix: " + f + " wine (k=" + str(k) + ")\n Classification error rate = "
                           + str(round(cer,3)), cer=cer, color=plt.cm.Purples)

    #Print classification report (to screen)
    print(cr)

    #Decision tree
    max_d=5 #This did not assist
    min_ss=10 #No
    min_sl=10 #No
    max_f=3 #Made a big difference - keep in
    max_ln=3 #No
    y = wineq.quality.values
    X = wineq[var].values
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=4)
    clf = DecisionTreeClassifier(max_features=max_f)
    fit = clf.fit(X_train,y_train)
    predicted = fit.predict(X_test)
    cm = confusion_matrix(y_test, predicted)
    cr = classification_report(y_test, predicted)

    #Calculate confusion error rate
    acc = accuracy_score(y_test, predicted)
    cer = 1-acc

    #Print confusion matrix
    print_confusion_matrix(cm, title="Decision tree confusion matrix: " + f + " wine \n" +
                           "(max features=" + str(max_f) + ")\n Classification error rate = "
                           + str(round(cer,3)), cer=cer, color=plt.cm.Oranges)

    #Print classification report (to screen)
    print(cr)


    #Naive Bayes
    y = wineq.quality.values
    X = wineq[var].values
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=4)
    clf = GaussianNB()
    fit = clf.fit(X_train,y_train)
    predicted = fit.predict(X_test)
    cm = confusion_matrix(y_test, predicted)
    cr = classification_report(y_test, predicted)
    
    #Calculate confusion error rate
    acc = accuracy_score(y_test, predicted)
    cer = 1-acc
    
    #Print confusion matrix
    print_confusion_matrix(cm, title="Naive Bayes confusion matrix: " + f + " wine \n Classification error rate = "
                           + str(round(cer,3)), cer=cer, color=plt.cm.Blues)

    #Print classification report (to screen)
    print(cr)


print("Modelling complete")
