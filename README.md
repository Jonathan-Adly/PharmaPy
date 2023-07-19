This is a python package that provides functionality for a Named-Entity Recognition (NER) model 
to identify names of pharmaceutical drugs within a text sample.


## Installation

The package can be installed from the command line with the following command

> pip install PharmaPy

## Sample Usage

`from PharmaPy import ner`

`text = "After surgery, David was given oxycodone for pain, prednisone to reduce inflammation, and benazepril for blood pressure control."`

`result = ner.predict(text)`
`print(result) #['oxycode', 'prednisone', benazepril]`


