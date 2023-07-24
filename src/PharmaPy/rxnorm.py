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


# This function takes any NDC-10 code (with or without hyphens) or NDC-11 code (with hyphens only) and returns the RxCUI
# numbers that can be used for other RxNorm functions. Some RxCUIs may return multiple RxCUI codes.
def get_rxcui_by_ndc(drug_ndc):
    url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?idtype=NDC&id={drug_ndc}"
    response = requests.get(url).json()

    drug_ndc_list = []
    for item in response["idGroup"]["rxnormId"]:
        drug_ndc_list.append(item)

    return drug_ndc_list


# This function takes a drug (input format as drug name, dose, dosage form; ex. lisinopril 20mg tablet or lisinopril
# 20 mg tablet) And returns a list of RxCUIs that can be used for other functions.
def get_rxcui_by_drug(drug):
    url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?name={drug}&search=1"
    response = requests.get(url).json()
    drug_rxcui_list = []
    for item in response["idGroup"]["rxnormId"]:
        drug_rxcui_list.append(item)
    return drug_rxcui_list


# This function takes the RxCUI and returns a drug name and dosage.
def get_rxnorm_name(rxcui):
    url = f"https://rxnav.nlm.nih.gov/REST/rxcui/{rxcui}.json"
    response = requests.get(url).json()

    return response["idGroup"]["name"]


