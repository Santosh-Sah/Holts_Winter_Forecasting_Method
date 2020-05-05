# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:53:28 2020

@author: Santosh Sah
"""
import pylab

def visualizeHoltsWinterForecastingMethodPredictedValues(holtsWinterForecastingMethodXTest, holtsWinterForecastingMethodXTrain,
                                                         holtsWinterForecastingMethodPredictedValues):
    #plotting the predicted values, training set and testing set
    holtsWinterForecastingMethodXTrain["Thousands of Passengers"].plot(legend = True, label = "Train")
    holtsWinterForecastingMethodXTest["Thousands of Passengers"].plot(legend = True, label = "Test")
    holtsWinterForecastingMethodPredictedValues.plot(legend = True, label = "PredictedValues")
    
    pylab.savefig('PredeictedValues.png')

def visualizeHoltsWinterForecastingMethodForecastedValues(holtsWinterForecastingMethodDataset, holtsWinterForecastingMethodForecastedValues):
    
    #plotting the forecated values with full dataset
    holtsWinterForecastingMethodDataset["Thousands of Passengers"].plot()
    
    holtsWinterForecastingMethodForecastedValues.plot()
    
    pylab.savefig('ForecastedValues.png')