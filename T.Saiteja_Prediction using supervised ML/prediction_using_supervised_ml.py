# -*- coding: utf-8 -*-
"""Prediction using supervised ML

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZB5KIvOEOpCZs93no0jt7z4fKCZjmSf

STEP 1-IMPORTING THE LIBRARIES INTO THE WORKSPACE
"""

#importing libraries
import numpy as np
import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt
import plotly.express as px
import scipy.stats as stats

"""STEP 2-IMPORTING THE DATASET INTO WORKSPACE"""

pr=pd.read_csv('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')
pr.head()

"""DESCRIBING THE DATA"""

pr.describe()

"""PLOTTING THE DISTRIBUTION OF DATA(SCORES) IN 2D GRAPH"""

#plotting the distribution of scores
plt.title('Hours vs percentage')
plt.xlabel('Hours studied')
plt.ylabel('percentage scored')
plt.scatter(pr.Hours,pr.Scores,color='Red',marker='.')

"""From the above graph we can state that there is positive relationship between the hours studied and the percentage scored"""

pr.shape

"""DATA PREPARATION

Taking x as the input variable 
Taking y as the target variable
"""

x=pr.iloc[:,:-1].values
y=pr.iloc[:,1].values

from sklearn.model_selection import train_test_split  #we use train_test_spilt because we cant train a model on a single data set even if we train we dont know its performance

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.3,random_state=1)

"""Completing the training of the data"""

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
print("Training complete")

line=regressor.coef_*x+regressor.intercept_
plt.scatter(x,y)
plt.plot(x,line);
plt.show()

print(x_test)  #testing data in hours
y_pred=regressor.predict(x_test) #prediciting the scores

#comparing the actual output values for x-test withpredicted values
pr = pd.DataFrame({'Actual': y_test,'Predicted': y_pred})
pr

#testing with our own data
hours=9.25
test=np.array([hours])
test=test.reshape(-1,1)
own_pred=regressor.predict(test)
print("No of hours = {}".format(hours))
print("Predicted scores = {}".format(own_pred[0]))

#evalvuating the model
from sklearn import metrics
print('Mean absolute Error: ',metrics.mean_absolute_error(y_test,y_pred))

"""if a student studies 9.25 hours per day the model predicts the 94 percent of the score"""
