# Placeholder function for text classification (replace this with your actual text classification model)
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd
import numpy as np
import csv
import os
import re

from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
cVectorize = CountVectorizer()

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import collections
from collections import defaultdict

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from tensorflow.python import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM

from tkinter import *
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
import scipy
def dataProcessorString(dfString):
# Performs text processing on a text string (a medical abstract) and returns processed string 
# for vectorizing for machine learning inference.
    lemmatizer = WordNetLemmatizer()

    tempDoc=dfString
    tempDoc=tempDoc.lower() # lower case
    tempDoc = tempDoc.split() # split into words
    tempDoc = [word for word in tempDoc if word not in stopwords.words('english')] # remove stops words
    tempDoc = [lemmatizer.lemmatize(word) for word in tempDoc] #Lemmatize
    tempDoc = ' '.join(tempDoc) # recreate the doc
    return tempDoc

def selectModel(modelID):
    if (modelID=='NB'):
        model_pkl_file  = "/Users/aliasgherdalal/Documents/Glia/models/NBTextClass.pkl"
    else:
        model_pkl_file = "/Users/aliasgherdalal/Documents/Glia/models/LRTextClass.pkl"
        
    vector_pkl_file = "/Users/aliasgherdalal/Documents/Glia/models/vectorizer.pickle"

    with open(model_pkl_file, 'rb') as file:  
        loadedModel = pickle.load(file)
    # load the vectorizer
    with open(vector_pkl_file, 'rb') as file:  
        loadedVectorizer = pickle.load(file)
    return loadedModel,loadedVectorizer
    
def currentCondition(classID):
    if (classID==1):
        conditionL='neoplasms'
    elif (classID==2):
        conditionL='digestive system diseases'        
    elif (classID==3):
        conditionL='nervous system diseases'        
    elif (classID==4):
        conditionL='cardiovascular diseases'        
    else:
        conditionL='general pathological conditions'
    return conditionL

def classify_text(text,modelID):
    text=dataProcessorString(text)
    #text=self.cVectorize.transform([text])
    loadedModel,loadedVectorizer = selectModel(modelID)
    y_predict =loadedModel.predict(loadedVectorizer.transform([text]))
    #print(modelUploaded.predict(loaded_vectorizer.transform([utt])))
    
    conditionL=currentCondition(y_predict[0])
    return y_predict[0],conditionL

    # Replace this logic with your text classification model
    # For demonstration purposes, returning a placeholder value
    