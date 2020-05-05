# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:52:22 2020

@author: Santosh Sah
"""

from HoltsWinterForecastingMethodUtils import (readHoltsWinterForecastingMethodXTest, readHoltsWinterForecastingMethodModel, 
                                               saveHoltsWinterForecastingMethodPredictedValues, readHoltsWinterForecastingMethodXTrain,
                                               readHoltsWinterForecastingMethodPredictedValues)
from HoltsWinterForecastingMethodVisualization import visualizeHoltsWinterForecastingMethodPredictedValues

"""
test the model on testing dataset
"""
def testHoltsWinterForecastingMethodModel():
    
    #reading model from pickle file
    holtsWinterForecastingMethodModel = readHoltsWinterForecastingMethodModel()
    
    #forecasting for 36 months
    predictedValues = holtsWinterForecastingMethodModel.forecast(36)
    
    #saving the foreasted values
    saveHoltsWinterForecastingMethodPredictedValues(predictedValues)

def plotHoltsWinterForecastingMethodPredictedValues():
    
    #reading testing set
    X_test = readHoltsWinterForecastingMethodXTest()
    
    #reading training set
    X_train = readHoltsWinterForecastingMethodXTrain()
    
    #reading predicted value
    predictedValues = readHoltsWinterForecastingMethodPredictedValues()
    
    #visualizing the predicted values with training set and the testing set
    visualizeHoltsWinterForecastingMethodPredictedValues(X_test, X_train,
                                                         predictedValues)
    
    
if __name__ == "__main__":
    #testHoltsWinterForecastingMethodModel()
    plotHoltsWinterForecastingMethodPredictedValues()