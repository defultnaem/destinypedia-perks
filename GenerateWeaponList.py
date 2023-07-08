import requests
import json
from datetime import datetime

def GetManifest():
    global manifest
    
    url = "https://www.bungie.net/Platform/Destiny2/Manifest"
    payload = {}
    headers = {
      'x-api-key': 'b51473b6521d458b8733d0844cd66f1f',
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    manifest = json.loads(response.content)

def GetItemDefinitionEndpoint():
    GetDestiny2EnManifestPath()

    response = requests.get(enManifestPath)

    today = datetime.today().strftime("%Y-%m-%d")
    filename = "d2Manifest_"+today+".json"

    print (today)
    print (filename)
    open(filename, "wb").write(response.content)

GetItemDefinitionEndpoint()
