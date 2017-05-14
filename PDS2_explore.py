#s3132392 Casey-Ann Charlesworth
#Assignment 2 - Practical Data Science
#Assignment due 18 May 2017


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files = ["red", "white"]
var = ["fixed acidity","volatile acidity","citric acid","residual sugar",
       "chlorides","free sulfur dioxide","total sulfur dioxide","density",
       "pH","sulphates","alcohol"]
class_var = ["quality"]


#import file and create summary graphs
for f in files:
    filename = f + ".csv"
    wineq = pd.read_csv(filename,sep=",",header=0)

    # quick overview of all variables - uncomment for submission
    wineq.plot.box(subplots=True, fontsize=9, layout=(4,3), figsize=(12,7), title="Boxplot of all variables: " + f + " wine")
    plt.show()

    wineq.plot.hist(subplots=True, fontsize=9, bins=25, layout=(4,3), figsize=(12,7), title="Histogram of all variables: " + f + " wine")
    plt.show()

    # a closer look at the class variable - uncomment for submission
    wineq[class_var].plot(kind="density", legend=False, title="Class variable (quality) density plot: " + f + " wine")
    plt.show()

    # exploring relationships between pairs - uncomment for submission
    wineq.plot.scatter(x="free sulfur dioxide", y="total sulfur dioxide", color="Green")
    plt.title("Wine quality: free vs total sulfur dioxide (" + f + " wine)")
    plt.show()

    wineq.plot.scatter(x="fixed acidity", y="volatile acidity", color="Red")
    plt.title("Wine quality: fixed acidity vs volatile acidity (" + f + " wine)")
    plt.show()

    wineq.plot.hexbin(x="citric acid", y="residual sugar", gridsize=6, colormap="Purples")
    plt.title("Wine quality:  citric acid v residual sugar (" + f + " wine)")
    plt.show()

    wineq.plot.hexbin(x="chlorides", y="sulphates", gridsize=6, colormap="Blues")
    plt.title("Wine quality:  chlorides v sulphates (" + f + " wine)")
    plt.show()

    wineq.plot.scatter(x="density", y="pH", color="Orange")
    plt.title("Wine quality:  density v pH (" + f + " wine)")
    plt.show()

    wineq.plot.hexbin(x="alcohol", y="quality", gridsize=6, colormap="Greens")
    plt.title("Wine quality:  alcohol (%) v quality (" + f + " wine)")
    plt.show()

    for v in var:
        wineq.boxplot(column=v, by=class_var, grid=False)
        plt.title("Wine quality: " + v + " v quality (" + f + " wine)")
        plt.ylabel(v)
        plt.xlabel("Quality rating")
        plt.show()

    #Finally, get value counts of the class variable to show balance
    print(wineq["quality"].value_counts())


print("Exploration complete")
