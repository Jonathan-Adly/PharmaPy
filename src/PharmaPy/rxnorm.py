import json
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


def get_all_matching_drug(partial_drug=None):
    drug_list = requests.get(
        "https://rxnav.nlm.nih.gov/REST/Prescribe/displaynames.json"
    ).json()["displayTermsList"]["term"]
    if partial_drug:
        drug_list = [drug.lower().strip() for drug in drug_list if partial_drug in drug]
    return drug_list


def get_rxcui_by_ndc(drug_ndc):
    """
    # This function takes any NDC-10 code (with or without hyphens) or NDC-11 code (with hyphens only) and returns the RxCUI
    # numbers that can be used for other RxNorm functions. Some RxCUIs may return multiple RxCUI codes.
    """
    url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?idtype=NDC&id={drug_ndc}"
    response = requests.get(url).json()

    drug_ndc_list = []
    for item in response["idGroup"]["rxnormId"]:
        drug_ndc_list.append(item)

    return drug_ndc_list


def get_rxcui_by_drug(drug):
    """
        This function takes a drug (input format as drug name, dose, dosage form; ex. lisinopril 20mg tablet or lisinopril
    20 mg tablet) And returns a list of RxCUIs that can be used for other functions.
    """
    url = f"https://rxnav.nlm.nih.gov/REST/rxcui.json?name={drug}&search=1"
    response = requests.get(url).json()
    drug_rxcui_list = []
    for item in response["idGroup"]["rxnormId"]:
        drug_rxcui_list.append(item)
    return drug_rxcui_list


def get_rxnorm_name(rxcui):
    # This function takes the RxCUI and returns a drug name and dosage.
    url = f"https://rxnav.nlm.nih.gov/REST/rxcui/{rxcui}.json"
    response = requests.get(url).json()

    return response["idGroup"]["name"]


def get_drug_class_by_name(drug_name, exact_match=False):
    url = f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byDrugName.json?drugName={drug_name}&relaSource=va"
    response = requests.get(url).json()
    # return [{"drug": "drug_name", "class": "class_name"}]
    results = []
    for item in response["rxclassDrugInfoList"]["rxclassDrugInfo"]:
        name = item["minConcept"]["name"]
        drug_class = item["rxclassMinConceptItem"]["className"]
        if exact_match:
            if name.lower() == drug_name.lower():
                results.append({"drug": name, "class": drug_class})
        else:
            results.append({"drug": name, "class": drug_class})
    # remove duplicates
    results = [dict(t) for t in {tuple(d.items()) for d in results}]
    return results


def get_drug_class_by_ndc(ndc):
    rxcuis = get_rxcui_by_ndc(ndc)
    results = []
    for rxcui in rxcuis:
        url = f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byRxcui.json?rxcui={rxcui}&relaSource=va"
        response = requests.get(url).json()

        for item in response["rxclassDrugInfoList"]["rxclassDrugInfo"]:
            drug_name = item["minConcept"]["name"]
            drug_class = item["rxclassMinConceptItem"]["className"]
            results.append({"drug": drug_name, "class": drug_class})
    # remove duplicates
    results = [dict(t) for t in {tuple(d.items()) for d in results}]
    return results


def get_fda_rxcuis(drug_name):
    url = f"https://rxnav.nlm.nih.gov/REST/drugs.json?name={drug_name}"
    response = requests.get(url).json()
    results = []
    for field in response["drugGroup"]["conceptGroup"]:
        if "conceptProperties" in field:
            for item in field["conceptProperties"]:
                results.append({item["name"]: item["rxcui"]})
    arr = []
    for value in results:
        rxcui = list(value.items())[0][1]
        api_url = f"https://api.fda.gov/drug/label.json?search=openfda.rxcui:{rxcui}"
        response = requests.get(api_url).json()
        if "error" not in response:
            arr.append(value)
    return arr
