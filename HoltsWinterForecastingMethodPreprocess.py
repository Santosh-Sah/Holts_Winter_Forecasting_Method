# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:51:38 2020

@author: Santosh Sah
"""

from HoltsWinterForecastingMethodUtils import (importHoltsWinterForecastingMethodDataset, saveTrainingAndTestingDataset, splitHoltsWinterForecastingMethodDataset)

def preprocess():
    
    holtsWinterForecastingMethodDataset = importHoltsWinterForecastingMethodDataset("airline_passengers.csv")
    
    X_train, X_test = splitHoltsWinterForecastingMethodDataset(holtsWinterForecastingMethodDataset)
    
    saveTrainingAndTestingDataset(X_train, X_test)
    

if __name__ == "__main__":
    preprocess()