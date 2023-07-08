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
    
def GetInventoryItemDefinition():
    global inventoryItemDefinition

    inventoryItemDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyInventoryItemDefinition"]
    inventoryItemDefinition = "https://bungie.net"+inventoryItemDefinition
    print(inventoryItemDefinition)

    
def GetSandboxPerkDefinition():
    global sandboxPerkDefinition

    sandboxPerkDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinySandboxPerkDefinition"]
    sandboxPerkDefinition = "https://bungie.net"+sandboxPerkDefinition
    print(sandboxPerkDefinition)

##response = requests.get(inventoryItemDefinition)

##filename = "d2Manifest_"+today+".json"

##print (filename)

    open(filename, "wb").write(response.content)

