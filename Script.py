# Script.py
import xml.etree.ElementTree as ET
import requests
import json
import numpy as np
import matplotlib.pyplot as plt

def zenodoResource(resource_id):
    api_base_url = "https://zenodo.org/api/records/"
    headers = {'accept': 'application/json'}
    r = requests.get(api_base_url+str(resource_id),headers)
    return json.loads(r.text)

resource = zenodoResource(3608992)
data = np.loadtxt(resource["files"][0]["links"]["self"])
plt.plot(data)
plt.ylabel('Amount of people')
plt.show()