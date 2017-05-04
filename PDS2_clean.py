#s3132392 Casey-Ann Charlesworth
#Assignment 2 - Practical Data Science
#Assignment due 18 May 2017


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files = ["red", "white"]
var = ["fixed acidity","volatile acidity","citric acid","residual sugar",
       "chlorides","free sulfur dioxide","total sulfur dioxide","density",
       "pH","sulphates","alcohol","quality"]
output = ["output.csv"]


#import file
for f in files:
    filename = "winequality-" + f + ".csv"
    wineq = pd.read_csv(filename,sep=";",header=0)

    #check variables - commented out for submission
    #print(wineq.dtypes)

    #check summary statistics - commented out for submission
    #print(wineq.describe(include="all"))
    
    #check for missing values - commented out for submission
    #for v in var:
    #    bad = wineq.loc[wineq[v] == np.nan]
    #    print(bad)
    
    wineq.to_csv(f + ".csv",sep=",", index=False, decimal=".")
    

print("Preprocessing complete")
