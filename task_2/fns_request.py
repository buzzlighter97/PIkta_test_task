import requests
import json
from pprint import pprint

def payee_details_request(ifns, oktmmf):
    data = {
        "npKind": "fl",
        "c": "next",
        "step": 1,
        "ifns": ifns,
        "oktmmf": oktmmf
    }
    response = requests.post("https://service.nalog.ru/addrno-proc.json", data)
    response_dict = json.loads(response.text)
    payee_details = response_dict["payeeDetails"]
    return payee_details

pprint(payee_details_request(7840, 40913000))