This is a python package that provides functionality for several useful utilities for drug information tasks. 

## Installation

The package can be installed from the command line with the following command

> pip install PharmaPy

We have the following modules:

## A Named-Entity Recognition (NER) machine learning model 

This extracts drug names from any text sample. Useful when you have medical notes, questions, or PDFs and you want to extract the drug name for further analysis. The model is very small wiht ~95% accuracy and can run locally or any modern CPU server. No complicated machine learning deployment needed.
### Sample Usage

`from PharmaPy import ner`

`text = "After surgery, David was given oxycodone for pain, prednisone to reduce inflammation, and benazepril for blood pressure control."`

`result = ner.predict(text)`

`print(result) #['oxycode', 'prednisone', 'benazepril']`

## NADAC 
This module performs several common tasks to get drug pricing based on the NADAC dataset. Useful when you have a list of NDCs or drug name and what to get how much they cost. 

### Sample Usage 

`from PharmaPy import nadac`

`ndc_list = ['24385005452','46122062978']`

`result = nadac.get_from_ndc_list(ndc_list)`

`print(results)`

```
"""
[{'ndc_description': '8HR ARTHRITIS PAIN ER 650 MG', 'ndc': '46122062978', 'nadac_per_unit': '0.06987', 'pricing_unit': 'EA', 'as_of_date': '2022-12-28'}, {'ndc_description': '12HR NASAL DECONGEST ER 120 MG', 'ndc': '24385005452', 'nadac_per_unit': '0.28255', 'pricing_unit': 'EA', 'as_of_date': '2022-12-28'}]
"""
```


## RXNORM
This module simplifies interactions with the RXNorm API. Useful to get supplemental drug information that may not be in the FDA label database.


### Sample Usage 

`from PharmaPy import rxnorm`

`drug = "atorvastatin" `

`formulation_containing_drug = rxnorm.get_all_formulations(drug)`

`print(formulation_containing_drug)`

```
"""
['atorvastatin 10 MG / ezetimibe 10 MG Oral Tablet [Lypqozet]', 'atorvastatin 20 MG / ezetimibe 10 MG Oral Tablet [Lypqozet]', 'atorvastatin 40 MG / ezetimibe 10 MG Oral Tablet [Lypqozet]', 'atorvastatin 80 MG / ezetimibe 10 MG Oral Tablet [Lypqozet]', 'atorvastatin 80 MG Oral Tablet [Lipitor]', 'atorvastatin 4 MG/ML Oral Suspension [Atorvaliq]', 'atorvastatin 10 MG Oral Tablet [Lipitor]', 'atorvastatin 20 MG Oral Tablet [Lipitor]', 'atorvastatin 40 MG Oral Tablet [Lipitor]', 'amlodipine 10 MG / atorvastatin 10 MG Oral Tablet [Caduet]', 'amlodipine 10 MG / atorvastatin 20 MG Oral Tablet [Caduet]', 'amlodipine 10 MG / atorvastatin 40 MG Oral Tablet [Caduet]', 'amlodipine 10 MG / atorvastatin 80 MG Oral Tablet [Caduet]', 'amlodipine 2.5 MG / atorvastatin 40 MG Oral Tablet [Caduet]', 'amlodipine 5 MG / atorvastatin 10 MG Oral Tablet [Caduet]', 'amlodipine 5 MG / atorvastatin 20 MG Oral Tablet [Caduet]', 'amlodipine 5 MG / atorvastatin 40 MG Oral Tablet [Caduet]', 'amlodipine 5 MG / atorvastatin 80 MG Oral Tablet [Caduet]', 'atorvastatin 10 MG / ezetimibe 10 MG Oral Tablet', 'atorvastatin 20 MG / ezetimibe 10 MG Oral Tablet', 'atorvastatin 40 MG / ezetimibe 10 MG Oral Tablet', 'atorvastatin 80 MG / ezetimibe 10 MG Oral Tablet', 'atorvastatin 80 MG Oral Tablet', 'atorvastatin 4 MG/ML Oral Suspension', 'amlodipine 5 MG / atorvastatin 80 MG Oral Tablet', 'amlodipine 10 MG / atorvastatin 80 MG Oral Tablet', 'amlodipine 10 MG / atorvastatin 20 MG Oral Tablet', 'amlodipine 2.5 MG / atorvastatin 10 MG Oral Tablet', 'amlodipine 2.5 MG / atorvastatin 20 MG Oral Tablet', 'amlodipine 5 MG / atorvastatin 10 MG Oral Tablet', 'amlodipine 5 MG / atorvastatin 20 MG Oral Tablet', 'amlodipine 5 MG / atorvastatin 40 MG Oral Tablet', 'amlodipine 10 MG / atorvastatin 10 MG Oral Tablet', 'amlodipine 10 MG / atorvastatin 40 MG Oral Tablet', 'amlodipine 2.5 MG / atorvastatin 40 MG Oral Tablet', 'atorvastatin 20 MG Oral Tablet', 'atorvastatin 40 MG Oral Tablet', 'atorvastatin 10 MG Oral Tablet']
"""
```