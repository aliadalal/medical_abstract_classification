# Medical Abstract Classification
## BUSINESS UNDERSTANDING & PROBLEM DESCRIPTION


The business goal is to develop an application that can categorize a medical abstract into one of the five conditions. Each class represent current medical condition of a patient. These conditions are:
| Class ID        | Condition     |
| ----------------|:-------------:| 
| 1               | neoplasms | 
| 2               | digestive system diseases      |   
| 3               | nervous system diseases      | 
| 4               | cardiovascular diseases      | 
| 5               | general pathological conditions      | 


To aid in the development of the application, dataset containing ~28k labelled abstracts is provided. 

Initial analysis shows that a text classification machine learning technique may be applied to develop an application, which when given an abstract will be capable of returning the most likely condition that the medical abstract is referring to in the text and hence the patient associated to the abstract is currently afflicted to.

## DATA PROCESSING & ANALYSIS

This section of the notebook processes data, analyses and prepares data for the next stage of classification i.e. machine learning modelling.

Data is ingested - in this case Kaggle dataset for medical abstracts is ingested. The data is then processed through various claeaning stages including removal of missing data. In addition, the abstract text is converted to lower case, and split into word tokens. The stopwords are then removed from the text and lemmatization is performed before putting the processed word tokens back into string. The string represent processed medical abstract ready for further processing.

Finally, the processed text is vectorized for input into the machine learnign model(s).
## MODELLING
Modeling section of the notebook models data using various techniques including Naive Bayes, Logistic Regression and LSTM. The section also displays the cost curve for the models.
## EVALUATION
The evaluation section displays the results of model performance including confusion matrix heatmap.
## SAVE
The save section saves the model and vectors to deployment directory using pickle, where it can be accessed by the application to serve up inference.

## INFERENCE APPLICATION
The inference application is a Flask based application that serves up a web page to select a model and input medical abstract for classification. The inference is requested using a REST api endpoint /classify.

#### FRONTEND COMPONENTS
1. index.html
2. results.html
3. stype.css
4. script.js
#### BACKEND COMPONENTS
1. app.py
2. text_classification_model.py

## INSTRUCTIONS

1. Download the repository.
2. From command line >>python /Glia/app.py
3. Server is accessible at 127.0.0.1:5000
4. Enter a medical abstract text and click classify to call inference API.

## INFERENCE SAMPLES
<img width="865" alt="Dashboard" src="https://github.com/aliadalal/medical_abstract_classification/assets/5640612/6101983f-b161-46a4-8c72-8d59b3f2a164">
<img width="964" alt="Dashboard 2" src="https://github.com/aliadalal/medical_abstract_classification/assets/5640612/2a4fb91e-0e8c-47e8-b4be-205d7ef66b47">
<img width="824" alt="Results 1" src="https://github.com/aliadalal/medical_abstract_classification/assets/5640612/9707be90-3c3c-4860-8dce-8698fe5f9d09">




