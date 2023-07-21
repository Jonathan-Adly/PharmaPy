import requests

def get_all_formulations(drug_name):
    url = f"https://rxnav.nlm.nih.gov/REST/drugs.json?name={drug_name}"
    response = requests.get(url).json()
 
    drug_names = []

    for item in response["drugGroup"]["conceptGroup"]:
        if "conceptProperties" in item:
            i = 0
            while i < len(item["conceptProperties"]):
                drug_names.append(item["conceptProperties"][i]["name"])
                i = i + 1

    return drug_names



