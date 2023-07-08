import requests
import json
from datetime import datetime

def GetDestiny2EnManifestPath():
    global enManifestPath
    
    url = "https://www.bungie.net/Platform/Destiny2/Manifest"
    payload = {}
    headers = {
      'x-api-key': 'b51473b6521d458b8733d0844cd66f1f',
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    manifest = json.loads(response.content)
    enManifestPath = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyInventoryItemDefinition"]
    enManifestPath = "https://bungie.net"+enManifestPath
    print(enManifestPath)

def GetItemDefinitionEndpoint():
    GetDestiny2EnManifestPath()

    response = requests.get(enManifestPath)

    today = datetime.today().strftime("%Y-%m-%d")
    filename = "d2Manifest_"+today+".json"

    print (today)
    print (filename)
    open(filename, "wb").write(response.content)

GetItemDefinitionEndpoint()
