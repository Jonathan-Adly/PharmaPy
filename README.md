This is a python package that provides functionality for several useful utilities for drug information tasks. 

## Installation

The package can be installed from the command line with the following command

> pip install PharmaPy

We have the following modules:

## A Named-Entity Recognition (NER) machine learning model 

This extracts drug names from any text sample. Useful when you have medical notes, questions, or PDFs and you want to extract the drug name for further analysis. The model is very small wiht ~95% accuracy and can run locally on any modern CPU server. No complicated machine learning deployment needed.
### Sample Usage

`from PharmaPy import ner`

`text = "After surgery, David was given oxycodone for pain, prednisone to reduce inflammation, and benazepril for blood pressure control."`

`result = ner.predict(text)`
`print(result) #['oxycode', 'prednisone', benazepril]`

## NADAC 
This module performs several common tasks to get drug pricing based on the NADAC dataset. Useful when you have a list of NDCs or drug name and what to get how much they cost. 

### Available functions

1. get_from_ndc_list: return latest NADAC price per unit from an ndc list
 
`from PharmaPy import nadac`

`ndc_list = ['24385005452','46122062978']`

`result = nadac.get_from_ndc_list(ndc_list)`

`print(results)`

```
"""
[{'ndc_description': '8HR ARTHRITIS PAIN ER 650 MG', 'ndc': '46122062978', 'nadac_per_unit': '0.06987', 'pricing_unit': 'EA', 'as_of_date': '2022-12-28'}, {'ndc_description': '12HR NASAL DECONGEST ER 120 MG', 'ndc': '24385005452', 'nadac_per_unit': '0.28255', 'pricing_unit': 'EA', 'as_of_date': '2022-12-28'}]
"""
```
2. get_avg_from_ndc_description: return average NADAC price across all NDCs for a drug.

`from PharmaPy import nadac`

`drug_name = 'atorvastatin' `

`result = nadac.get_avg_from_ndc_description(drug_name)`

`print(results)`

```
"""
[{'ndc_description': 'ATORVASTATIN 80 MG TABLET', 'average_nadac_per_unit': '0.08744'}, {'ndc_description': 'ATORVASTATIN 40 MG TABLET', 'average_nadac_per_unit': '0.05733'}, {'ndc_description': 'ATORVASTATIN 20 MG TABLET', 'average_nadac_per_unit': '0.04069'}, {'ndc_description': 'ATORVASTATIN 10 MG TABLET', 'average_nadac_per_unit': '0.03081'}]
"""






