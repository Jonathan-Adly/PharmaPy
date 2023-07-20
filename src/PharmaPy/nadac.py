import requests
import json


def get_from_ndc_list(ndc_list):
    """
    This function takes a list of ndcs and returns the latest NADAC per unit for each ndc
    """
    if not ndc_list:
        return []
    
    url = "https://data.medicaid.gov/api/1/datastore/query/dfa2ab14-06c2-457a-9e36-5cb6d80f8d93/0/"
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
                "property": "ndc",
                "value": ndc_list,
                "operator": "in",
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
    results = json.loads(response)["results"]
    seen = []
    new_list = []

    for item in results:
        if not item["ndc_description"] in seen:
            new_list.append(item)
            seen.append(item["ndc_description"])
    
    return new_list