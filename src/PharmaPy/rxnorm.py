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
    rxcui = requests.get(
        f"https://rxnav.nlm.nih.gov/REST/ndcstatus.json?ndc={ndc}"
    ).json()["ndcStatus"]["rxcui"]
    url = f"https://rxnav.nlm.nih.gov/REST/rxclass/class/byRxcui.json?rxcui={rxcui}&relaSource=va"
    response = requests.get(url).json()
    results = []
    for item in response["rxclassDrugInfoList"]["rxclassDrugInfo"]:
        drug_name = item["minConcept"]["name"]
        drug_class = item["rxclassMinConceptItem"]["className"]
        results.append({"drug": drug_name, "class": drug_class})
    # remove duplicates
    results = [dict(t) for t in {tuple(d.items()) for d in results}]
    return results
