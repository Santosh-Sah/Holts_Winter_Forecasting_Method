# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:51:54 2020

@author: Santosh Sah
"""
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from HoltsWinterForecastingMethodUtils import (saveHoltsWinterForecastingMethodModel, readHoltsWinterForecastingMethodXTrain, 
                                               importHoltsWinterForecastingMethodDataset, saveHoltsWinterForecastingMethodModelForFullDataset)

"""
Train HoltsWinterForecastingMethod model on training set
"""
def trainHoltsWinterForecastingMethodModel():
    
    X_train = readHoltsWinterForecastingMethodXTrain()
    
    #training model on the training set
    holtsWinterForecastingMethodModel = ExponentialSmoothing(X_train["Thousands of Passengers"], 
                                                             trend = "mul",
                                                             seasonal = "mul",
                                                             seasonal_periods = 12).fit()
    
    saveHoltsWinterForecastingMethodModel(holtsWinterForecastingMethodModel)

"""
Train HoltsWinterForecastingMethod model on full dataset
"""
def trainHoltsWinterForecastingMethodModelOnFullDataset():
    
    holtsWinterForecastingMethodDataset = importHoltsWinterForecastingMethodDataset("airline_passengers.csv")
    
    #training model on the whole dataset
    holtsWinterForecastingMethodModel = ExponentialSmoothing(holtsWinterForecastingMethodDataset["Thousands of Passengers"], 
                                                             trend = "mul",
                                                             seasonal = "mul",
                                                             seasonal_periods = 12).fit()
    
    saveHoltsWinterForecastingMethodModelForFullDataset(holtsWinterForecastingMethodModel)

if __name__ == "__main__":
    #trainHoltsWinterForecastingMethodModel()
    trainHoltsWinterForecastingMethodModelOnFullDataset()    
