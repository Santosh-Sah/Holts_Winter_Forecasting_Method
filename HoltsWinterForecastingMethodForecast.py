# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:52:57 2020

@author: Santosh Sah
"""

from HoltsWinterForecastingMethodUtils import (importHoltsWinterForecastingMethodDataset, saveHoltsWinterForecastingMethodForecastedValues,
                                               readHoltsWinterForecastingMethodForecastedValues, readHoltsWinterForecastingMethodModelForFullDataset)
from HoltsWinterForecastingMethodVisualization import visualizeHoltsWinterForecastingMethodForecastedValues

def forecastWithHoltsWinterForecastingMethodModel():
    
    #reading the model whichis trained on the whole dataset
    holtsWinterForecastingMethodModel = readHoltsWinterForecastingMethodModelForFullDataset()
    
    #foresting for 36 months
    holtsWinterForecastingMethodForecastedValues = holtsWinterForecastingMethodModel.forecast(36)
    
    #saving the forecasted values
    saveHoltsWinterForecastingMethodForecastedValues(holtsWinterForecastingMethodForecastedValues)

def plotHoltsWinterForecastingMethodForecastedValues():
    
    #reading the dataset
    holtsWinterForecastingMethodDataset = importHoltsWinterForecastingMethodDataset("airline_passengers.csv")
    
    #reading the forecated values
    holtsWinterForecastingMethodForecastedValues = readHoltsWinterForecastingMethodForecastedValues()
    
    #visualizing the forecated values
    visualizeHoltsWinterForecastingMethodForecastedValues(holtsWinterForecastingMethodDataset, holtsWinterForecastingMethodForecastedValues)

if __name__ == "__main__":
    #forecastWithHoltsWinterForecastingMethodModel()
    plotHoltsWinterForecastingMethodForecastedValues()
    