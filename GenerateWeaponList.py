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

def GenerateWeaponList():
    GetInventoryItemDefinition()
    
def GetSandboxPerkDefinition():
    global sandboxPerkDefinition

    sandboxPerkDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinySandboxPerkDefinition"]
    sandboxPerkDefinition = "https://bungie.net"+sandboxPerkDefinition
    print(sandboxPerkDefinition)

def GeneratePerksList():
    GetSandboxPerkDefinition()
    
GetManifest()
GenerateWeaponList()
GeneratePerksList()

##response = requests.get(inventoryItemDefinition)

today = datetime.today().strftime("%Y-%m-%d")
##filename = "d2Manifest_"+today+".json"

print (today)
##print (filename)

def GenerateWeaponAndPerkFile():
    open(filename, "wb").write(response.content)

