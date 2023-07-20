import requests

url = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=azithromycin"
response = requests.get(url)
print(response.json())