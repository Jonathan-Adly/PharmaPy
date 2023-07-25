import requests
import json
import itertools
from decimal import Decimal


def get_from_ndc_list(ndc_list):
    """
    This function takes a list of ndcs and returns the latest NADAC per unit for each ndc
    """
    if not ndc_list:
        return []

    url = "https://data.medicaid.gov/api/1/datastore/query/4a00010a-132b-4e4d-a611-543c9521280f/0/"
    payload = {
        "keys": "true",
        "offset": "0",
        "properties": [
            "ndc_description",
            "ndc",
            "nadac_per_unit",
            "pricing_unit",
            "as_of_date",
            "effective_date",
        ],
        "conditions": [
            {
                "property": "ndc",
                "value": ndc_list,
                "operator": "in",
            }
        ],
        "sorts": [
            {"property": "effective_date", "order": "desc"},
            {"property": "ndc_description", "order": "desc"},
        ],
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, json=payload, headers=headers).content
    results = json.loads(response)["results"]
    seen = []
    new_list = []

    for item in results:
        if not item["ndc_description"] in seen:
            new_list.append(item)
            seen.append(item["ndc_description"])

    return new_list


def get_avg_from_ndc_description(drug_name, exact_match=False, starts_with=False):
    """
    This function takes a drug name and returns the average NADAC per unit for that drug
    across all ndcs that match the drug name on the latest nadac files.
    default matching behavir is "contain", but you can also match on starts_with (by setting starts_with to True) or exact (by setting exact_match to True).
    """
    if exact_match and starts_with:
        raise ValueError("Cannot have exact_match and starts_with both be True")

    if exact_match:
        operator = "is"
    elif starts_with:
        operator = "starts with"
    else:
        operator = "contains"

    url = "https://data.medicaid.gov/api/1/datastore/query/4a00010a-132b-4e4d-a611-543c9521280f/0/"
    payload = {
        "keys": "true",
        "offset": "0",
        "properties": [
            "ndc_description",
            "ndc",
            "nadac_per_unit",
            "pricing_unit",
            "as_of_date",
        ],
        "conditions": [
            {
                "property": "ndc_description",
                "value": drug_name,
                "operator": operator,
            }
        ],
        "sorts": [
            {"property": "as_of_date", "order": "desc"},
            {"property": "ndc_description", "order": "desc"},
        ],
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, json=payload, headers=headers).content
    try:
        results = json.loads(response)["results"]
    except KeyError:
        return []

    seen = []
    new_list = []

    for item in results:
        if not item["ndc"] in seen:
            new_list.append(item)
            seen.append(item["ndc"])

    new_list = [
        list(v)
        for k, v in itertools.groupby(new_list, key=lambda k: k["ndc_description"])
    ]

    result = []
    for name_list in new_list:
        total = 0
        description = name_list[0]["ndc_description"]
        for item in name_list:
            total += Decimal(item["nadac_per_unit"])

        average = total / len(name_list)
        result.append(
            {"ndc_description": description, "average_nadac_per_unit": str(average)}
        )
    return result
