# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:50:57 2020

@author: Santosh Sah
"""
import pandas as pd
import pickle
"""
Import dataset and read specific column. Split the dataset in training and testing set.
"""
def importHoltsWinterForecastingMethodDataset(holtsWinterForecastingMethodDatasetFileName):
    
    holtsWinterForecastingMethodDataset = pd.read_csv(holtsWinterForecastingMethodDatasetFileName,index_col='Month',parse_dates=True)
    
    #the dataset is minthly dataset. Hence setting its frequency as monthly.
    holtsWinterForecastingMethodDataset.index.freq = "MS"
    
    return holtsWinterForecastingMethodDataset

#splitting dataset into training and testing set
def splitHoltsWinterForecastingMethodDataset(holtsWinterForecastingMethodDataset):
    
    #splitting the dataset into training and testing set.
    holtsWinterForecastingMethodTrainingSet = holtsWinterForecastingMethodDataset.iloc[:108]
    holtsWinterForecastingMethodTestingSet = holtsWinterForecastingMethodDataset.iloc[108:]
    
    return holtsWinterForecastingMethodTrainingSet, holtsWinterForecastingMethodTestingSet

"""
Save training and testing dataset
"""
def saveTrainingAndTestingDataset(X_train, X_test):
    
    #Write X_train in a picke file
    with open("X_train.pkl",'wb') as X_train_Pickle:
        pickle.dump(X_train, X_train_Pickle, protocol = 2)
    
    #Write X_test in a picke file
    with open("X_test.pkl",'wb') as X_test_Pickle:
        pickle.dump(X_test, X_test_Pickle, protocol = 2)

"""
read X_train from pickle file
"""
def readHoltsWinterForecastingMethodXTrain():
    
    #load X_train
    with open("X_train.pkl","rb") as X_train_pickle:
        X_train = pickle.load(X_train_pickle)
    
    return X_train

"""
read X_test from pickle file
"""
def readHoltsWinterForecastingMethodXTest():
    
    #load X_test
    with open("X_test.pkl","rb") as X_test_pickle:
        X_test = pickle.load(X_test_pickle)
    
    return X_test

"""
Save HoltsWinterForecastingMethod as a pickle file.
"""
def saveHoltsWinterForecastingMethodModel(holtsWinterForecastingMethodModel):
    
    #Write HoltsWinterForecastingMethodModel as a picke file
    with open("holtsWinterForecastingMethodModel.pkl",'wb') as HoltsWinterForecastingMethodModel_Pickle:
        pickle.dump(holtsWinterForecastingMethodModel, HoltsWinterForecastingMethodModel_Pickle, protocol = 2)

"""
read HoltsWinterForecastingMethod from pickle file
"""
def readHoltsWinterForecastingMethodModel():
    
    #load HoltsWinterForecastingMethodModel model
    with open("HoltsWinterForecastingMethodModel.pkl","rb") as HoltsWinterForecastingMethodModel:
        holtsWinterForecastingMethodModel = pickle.load(HoltsWinterForecastingMethodModel)
    
    return holtsWinterForecastingMethodModel

"""
Save HoltsWinterForecastingMethod as a pickle file.
"""
def saveHoltsWinterForecastingMethodModelForFullDataset(holtsWinterForecastingMethodModelForFullDataset):
    
    #Write HoltsWinterForecastingMethodModelForFullDataset as a picke file
    with open("holtsWinterForecastingMethodModelForFullDataset.pkl",'wb') as HoltsWinterForecastingMethodModelForFullDataset_Pickle:
        pickle.dump(holtsWinterForecastingMethodModelForFullDataset, HoltsWinterForecastingMethodModelForFullDataset_Pickle, protocol = 2)

"""
read HoltsWinterForecastingMethod from pickle file
"""
def readHoltsWinterForecastingMethodModelForFullDataset():
    
    #load HoltsWinterForecastingMethodModelForFullDataset model
    with open("HoltsWinterForecastingMethodModelForFullDataset.pkl","rb") as HoltsWinterForecastingMethodModelForFullDataset:
        holtsWinterForecastingMethodModelForFullDataset = pickle.load(HoltsWinterForecastingMethodModelForFullDataset)
    
    return holtsWinterForecastingMethodModelForFullDataset

"""
save saveHoltsWinterForecastingMethodPredictedValues as a pickle file
"""

def saveHoltsWinterForecastingMethodPredictedValues(holtsWinterForecastingMethodPredictedValues):
    
    #Write HoltsWinterForecastingMethodPredictedValues in a picke file
    with open("HoltsWinterForecastingMethodPredictedValues.pkl",'wb') as holtsWinterForecastingMethodPredictedValues_Pickle:
        pickle.dump(holtsWinterForecastingMethodPredictedValues, holtsWinterForecastingMethodPredictedValues_Pickle, protocol = 2)

"""
read HoltsWinterForecastingMethodPredictedValues from pickle file
"""
def readHoltsWinterForecastingMethodPredictedValues():
    
    #load HoltsWinterForecastingMethodPredictedValues
    with open("HoltsWinterForecastingMethodPredictedValues.pkl","rb") as holtsWinterForecastingMethodPredictedValues_pickle:
        holtsWinterForecastingMethodPredictedValues = pickle.load(holtsWinterForecastingMethodPredictedValues_pickle)
    
    return holtsWinterForecastingMethodPredictedValues

"""
save saveHoltsWinterForecastingMethodForecastedValues as a pickle file
"""

def saveHoltsWinterForecastingMethodForecastedValues(holtsWinterForecastingMethodForecastedValues):
    
    #Write HoltsWinterForecastingMethodForecastedValues in a picke file
    with open("HoltsWinterForecastingMethodForecastedValues.pkl",'wb') as holtsWinterForecastingMethodForecastedValues_Pickle:
        pickle.dump(holtsWinterForecastingMethodForecastedValues, holtsWinterForecastingMethodForecastedValues_Pickle, protocol = 2)

"""
read HoltsWinterForecastingMethodForecastedValues from pickle file
"""
def readHoltsWinterForecastingMethodForecastedValues():
    
    #load HoltsWinterForecastingMethodForecastedValues
    with open("HoltsWinterForecastingMethodForecastedValues.pkl","rb") as holtsWinterForecastingMethodForecastedValues_pickle:
        holtsWinterForecastingMethodForecastedValues = pickle.load(holtsWinterForecastingMethodForecastedValues_pickle)
    
    return holtsWinterForecastingMethodForecastedValues


