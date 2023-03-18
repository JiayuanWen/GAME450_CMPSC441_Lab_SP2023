""" Lab 10: Save people
You can save people from heart disease by training a model to predict whether a person has heart disease or not.
The dataset is available at src/lab8/heart.csv
Train a model to predict whether a person has heart disease or not and test its performance.
You can usually improve the model by normalizing the input data. Try that and see if it improves the performance. 
"""
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# Models
# Source: https://scikit-learn.org/stable/supervised_learning.html#supervised-learning
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier

import pandas as pd
import numpy as np

data = pd.read_csv("src/lab10/heart.csv")

# Transform the categorical variables into dummy variables.
print(data.head())
string_col = data.select_dtypes(include="object").columns

df = pd.get_dummies(data, columns=string_col, drop_first=False)
y = df.HeartDisease.values
x = df.drop(["HeartDisease"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=25
)

print("")
print(data.head())

""" Improve the model by normalizing the input data. """
 # Normalized copy of original dataset
df_nor= (df-df.min()) / (df.max()-df.min())
y_nor = df_nor.HeartDisease.values
x_nor = df_nor.drop(["HeartDisease"], axis=1)
x_nor_train, x_nor_test, y_nor_train, y_nor_test = train_test_split(
    x_nor, y_nor, test_size=0.2, random_state=25
)

# Accuracy

print("")
print("----------------- KNeighbors Classifier -----------------")

""" Train a sklearn model here. """
sklearn_model = KNeighborsClassifier(n_neighbors=9)
sklearn_model = sklearn_model.fit(x_train,y_train)

print("\nAccuracy of model: {}".format(sklearn_model.score(x_test, y_test)))

sklearn_model = sklearn_model.fit(x_nor_train, y_nor_train)

print("Accuracy of improved model: {}\n".format(sklearn_model.score(x_nor_test, y_nor_test)))


print("")
print("----------------- Support Vector Classifier -----------------")

""" Train a sklearn model here. """
sklearn_model = svm.SVC()
sklearn_model = sklearn_model.fit(x_train,y_train)

print("\nAccuracy of model: {}".format(sklearn_model.score(x_test, y_test)))

sklearn_model = sklearn_model.fit(x_nor_train, y_nor_train)

print("Accuracy of improved model: {}\n".format(sklearn_model.score(x_nor_test, y_nor_test)))


print("")
print("----------------- Stochastic Gradient Descent Classifier -----------------")

""" Train a sklearn model here. """
sklearn_model = SGDClassifier(loss="hinge", penalty="l2", max_iter=1000)
sklearn_model = sklearn_model.fit(x_train,y_train)

print("\nAccuracy of model: {}".format(sklearn_model.score(x_test, y_test)))

sklearn_model = sklearn_model.fit(x_nor_train, y_nor_train)

print("Accuracy of improved model: {}\n".format(sklearn_model.score(x_nor_test, y_nor_test)))


print("")
print("----------------- Decision Tree Classifier -----------------")

""" Train a sklearn model here. """
sklearn_model = tree.DecisionTreeClassifier()
sklearn_model = sklearn_model.fit(x_train,y_train)

print("\nAccuracy of model: {}".format(sklearn_model.score(x_test, y_test)))

sklearn_model = sklearn_model.fit(x_nor_train, y_nor_train)

print("Accuracy of improved model: {}\n".format(sklearn_model.score(x_nor_test, y_nor_test)))


print("")
print("----------------- Neural Network (Supervised) Classifier -----------------")

""" Train a sklearn model here. """
sklearn_model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1, max_iter=1000)
sklearn_model = sklearn_model.fit(x_train,y_train)

print("\nAccuracy of model: {}".format(sklearn_model.score(x_test, y_test)))

sklearn_model = sklearn_model.fit(x_nor_train, y_nor_train)

print("Accuracy of improved model: {}\n".format(sklearn_model.score(x_nor_test, y_nor_test)))