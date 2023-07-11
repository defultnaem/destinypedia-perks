import requests
import json
import os
import time
from zipfile import ZipFile
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
    headers = {}
    manifestContent = manifest["Response"]["mobileWorldContentPaths"]["en"]
    destinyManifest = manifestContent
    manifestContent = requests.request("GET", "https://bungie.net"+manifestContent, headers=headers, data=payload)
    manifestFileName = "DestinyManifest_"+today+".zip"
    open(manifestFileName, "wb").write(manifestContent.content)
    time.sleep(3)
    destinyManifest = destinyManifest.replace("/common/destiny2_content/sqlite/en/", "")
    ZipFile(manifestFileName, "r").extract(destinyManifest, path=None)
    time.sleep(3)
    os.rename(destinyManifest, "manifest_archive/DestinyManifest_"+today+".sqlite3")
    os.remove(manifestFileName)
    
def GetInventoryItemDefinition():
    global inventoryItemDefinition
    payload = {}
    headers = {}

    inventoryItemDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyInventoryItemDefinition"]
    inventoryItemDefinition = requests.request("GET", "https://bungie.net"+inventoryItemDefinition, headers=headers, data=payload)
    open("DestinyInventoryItemDefinition.json", "wb").write(inventoryItemDefinition.content)
    
def GetSandboxPerkDefinition():
    global sandboxPerkDefinition
    payload = {}
    headers = {}

    sandboxPerkDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinySandboxPerkDefinition"]
    sandboxPerkDefinition = requests.request("GET", "https://bungie.net"+sandboxPerkDefinition, headers=headers, data=payload)
    open("DestinySandboxPerkDefinition.json", "wb").write(sandboxPerkDefinition.content)

def GetPlugSetDefinition():
    global plugSetDefinition
    payload = {}
    headers = {}

    plugSetDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyPlugSetDefinition"]
    plugSetDefinition = requests.request("GET", "https://bungie.net"+plugSetDefinition, headers=headers, data=payload)
    open("DestinyPlugSetDefinition.json", "wb").write(plugSetDefinition.content)

##today = datetime.today().strftime("%Y-%m-%d")
today = "2023-06-27"

GetManifest()
GetInventoryItemDefinition()
GetSandboxPerkDefinition()
GetPlugSetDefinition()

