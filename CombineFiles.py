import json
import os
import time

weaponFileName = "DestinyWeaponDefinition.json"
plugSetFileName = "DestinyPlugSetDefinition.json"
perkFileName = "DestinyPerkDefinition.json"
socketTypeFileName = "DestinySocketTypeDefinition.json"

def CombineFiles():
    weapon_list     = []
    plugSet_list    = []
    perk_list       = []
    socketType_list = []

    with open(weaponFileName, "r", encoding="utf-8") as weaponFile:
        weapon_list = json.load(weaponFile)
##    with open(plugSetFileName, "r", encoding="utf-8") as plugSetFile:
##        plugSet_list = json.load(plugSetFile)
##    with open(perkFileName, "r", encoding="ANSI") as perkFile:
##        perk_list = json.load(perkFile)
##    with open(socketTypeFileName, "r", encoding="utf-8") as socketTypeFile:
##        socketType_list = json.load(socketTypeFile)

##    print(weapon_list[0])
    
CombineFiles()
