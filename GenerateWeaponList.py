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
    payload = {}
    headers = {}

    inventoryItemDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyInventoryItemDefinition"]
##    print("https://bungie.net"+inventoryItemDefinition)
    inventoryItemDefinition = requests.request("GET", "https://bungie.net"+inventoryItemDefinition, headers=headers, data=payload)
##    inventoryItemDefinition = json.loads(inventoryItemDefinition.content) 
    
def GetSandboxPerkDefinition():
    global sandboxPerkDefinition

    sandboxPerkDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinySandboxPerkDefinition"]
    sandboxPerkDefinition = "https://bungie.net"+sandboxPerkDefinition
##    print(sandboxPerkDefinition)

def GetPlugSetDefinition():
    global plugSetDefinition

    plugSetDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyPlugSetDefinition"]
    plugSetDefinition = "https://bungie.net"+plugSetDefinition
##    print(plugSetDefinition)

def GeneratePerksList():
    GetSandboxPerkDefinition()

def GenerateWeaponList():
    GetInventoryItemDefinition()

def GeneratePlugSetList():
    GetPlugSetDefinition()
    
GetManifest()
GenerateWeaponList()
GeneratePerksList()
GeneratePlugSetList()

##response = requests.get(inventoryItemDefinition)

today = datetime.today().strftime("%Y-%m-%d")
filename = "d2Manifest_"+today+".json"

##print (today)
##print (filename)

def GenerateWeaponAndPerkFile():
    open(filename, "wb").write(inventoryItemDefinition.content)

GenerateWeaponAndPerkFile()
##print()
##print()
##print()

##with open(inventoryItemDefinition, "r") as data_file:
##    data = json.load(data_file)
##weaponItemType = inventoryItemDefinition["itemType"]

##for v in inventoryItemDefinition:
##    if weaponItemType == '3':
##        print(inventoryItemDefinition["displayProperties"]["name"])


        
