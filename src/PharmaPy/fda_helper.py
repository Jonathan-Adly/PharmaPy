import requests, re
import json
from bs4 import BeautifulSoup

def drug_information(drug_name, route):
    """
    This function takes a drug name and route and provides information about the drug
    """

    if not drug_name or not route:
        return []
    
    base_url = "https://api.fda.gov/drug/label.json"
    search_query = f"search=openfda.generic_name:\"{drug_name}\"+AND+openfda.route:\"{route}\""
    api_url = f"{base_url}?{search_query}"
    response = requests.get(api_url)

    if response.status_code != 200:
        return None
    
    res = response.json()
    newDict = {}

    for metric in res["results"]:
        for key in metric:
            arr = metric[key]
            
            # Normal Case
            if type(arr) != str and len(arr) == 1:

                if key == "clinical_studies_table":
                        newDict[key] = extract(str(arr[0]))
                else:
                    newDict[key] = str(arr[0])

            # Other Case - Tables or openfda
            elif type(arr) != str and len(arr) != 1:
                # openfda special case
                if key == "openfda":
                    for val in metric[key]:
                        if val != "package_ndc":
                            newDict[val] = str(metric[key][val][0])
                        else:
                            newDict[val] = metric[key][val]
                # tables
                else:
                    newDict[key] = (extract(str(metric[key]))[2:-3])

                
    return newDict

def extract(html_string):
    '''
    Extracts the text from an HTML string
    '''
    soup = BeautifulSoup(html_string, 'html.parser')
    return soup.get_text()


def drug_field(drug_name, route, field):
    '''
    Returns a particular field name
    '''
    res = drug_information(drug_name, route)
    if field in res:
        return res[field]
    else:
        return None


# drug_information("ciprofloxacin", "oral")
# drug_field("ciprofloxacin", "oral", "spl_product_data_elements")