import requests
import json


def get_all_formulations(drug_name):
    url = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" + drug_name
    response = requests.get(url)
    var = json.loads(response.text)
    drug_names = []

    for item in var["drugGroup"]["conceptGroup"]:
        if "conceptProperties" in item:
            i = 0
            while i < len(item["conceptProperties"]):
                drug_names.append(item["conceptProperties"][i]["name"])
                i = i + 1

    print(json.dumps(drug_names, indent=4))


get_all_formulations("acetaminophen")


# Use this code to test getting REST API for certain drugs.
# url = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=lisinopril"
# var = json.loads(requests.get(url).text)
# print(json.dumps(var, indent=4))
