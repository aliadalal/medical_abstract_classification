# medical_abstract_classification
**Business Understanding and Problem Description
**
The business goal is to develop an application that can categorize a medical abstract into one of the five conditions. Each class represent current medical condition of a patient. These conditions are:  
These classes 
    1	neoplasms
	2	digestive system diseases
	3	nervous system diseases
	4	cardiovascular diseases
	5	general pathological conditions
To aid in the development of the application, dataset containing ~28k labelled abstracts is provided. 

Initial analysis shows that a text classification machine learning technique may be applied to develop an application, which when given an abstract will be capable of returning the most likely condition that the medical abstract is referring to in the text and hence the patient associated to the abstract is currently afflicted to.

**Data Processing and Analysis
**
This section of the notebook processes data, analyses and prepares data for the next stage of classification i.e. machine learning modelling.

Data is ingested - in this case Kaggle dataset for medical abstracts is ingested. The data is then processed through various claeaning stages including removal of missing data. In addition, the abstract text is converted to lower case, and split into word tokens. The stopwords are then removed from the text and lemmatization is performed before putting the processed word tokens back into string. The string represent processed medical abstract ready for further processing.

Finally, the processed text is vectorized for input into the machine learnign model(s).
