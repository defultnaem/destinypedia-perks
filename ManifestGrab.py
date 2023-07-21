import requests
import json
import os
import time
from zipfile import ZipFile
from datetime import datetime
import GenerateNewFiles as gnf

def GetManifest():
    global manifest
    
    url = "https://www.bungie.net/Platform/Destiny2/Manifest"
    payload = {}
    headers = {
      'x-api-key': 'b51473b6521d458b8733d0844cd66f1f',
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    manifest = json.loads(response.content)
    print("manifest pulled")
    headers = {}
    manifestContent = manifest["Response"]["mobileWorldContentPaths"]["en"]
    destinyManifest = manifestContent
    manifestContent = requests.request("GET", "https://bungie.net"+manifestContent, headers=headers, data=payload)
    manifestFileName = "DestinyManifest_"+today+".zip"
    open(manifestFileName, "wb").write(manifestContent.content)
    time.sleep(3)
    print("manifest saved")
    destinyManifest = destinyManifest.replace("/common/destiny2_content/sqlite/en/", "")
    ZipFile(manifestFileName, "r").extract(destinyManifest, path=None)
    time.sleep(3)
    print("files extracted from .zip")
    os.rename(destinyManifest, "manifest_archive/DestinyManifest_"+today+".sqlite3")
    print(".content file renamed")
    print(".content file moved")
    os.remove(manifestFileName)
    print(".zip file removed")
    
def GetInventoryItemDefinition():
    global inventoryItemDefinition
    payload = {}
    headers = {}

    inventoryItemDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyInventoryItemDefinition"]
    inventoryItemDefinition = requests.request("GET", "https://bungie.net"+inventoryItemDefinition, headers=headers, data=payload)
    open("DestinyInventoryItemDefinition.json", "wb").write(inventoryItemDefinition.content)
    print("item file generated")

def GetPlugSetDefinition():
    global plugSetDefinition
    payload = {}
    headers = {}

    plugSetDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyPlugSetDefinition"]
    plugSetDefinition = requests.request("GET", "https://bungie.net"+plugSetDefinition, headers=headers, data=payload)
    open("DestinyPlugSetDefinition.json", "wb").write(plugSetDefinition.content)
    print("plug set file generated")

def GetSocketTypeDefinition():
    global socketTypeDefinition
    payload = {}
    headers = {}

    socketTypeDefinition = manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinySocketTypeDefinition"]
    socketTypeDefinition = requests.request("GET", "https://bungie.net"+socketTypeDefinition, headers=headers, data=payload)
    open("DestinySocketTypeDefinition.json", "wb").write(socketTypeDefinition.content)
    print("socket type file generated")

def RemoveOldFiles():
    os.remove("DestinyWeaponDefinition.json")
    os.remove("DestinyPerkDefinition.json")
    os.remove("DestinyPlugSetDefinition.json")
    os.remove("DestinySocketTypeDefinition.json")
    time.sleep(3)
    
today = datetime.today().strftime("%Y-%m-%d")
##today = "2023-06-27"

RemoveOldFiles()
GetManifest()
GetInventoryItemDefinition()
GetSocketTypeDefinition()
GetPlugSetDefinition()
gnf.GenerateWeaponList()
gnf.GeneratePerkList()
gnf.DeleteItemFile()
