import json
import os
import re
import jsbeautifier as jsb

file_name = "DestinyInventoryItemDefinition.json"

def GenerateWeaponList():
    weapon_list = []
    hash_list = []

    with open(file_name, "rb") as f:
        my_list = json.load(f)

        for idx, obj in my_list.items():
            if obj != None:
                if obj["itemType"] == 3:
                    weapon_list.append(obj)
                    hash_list.append(obj["hash"])

    weapon_file_name = "DestinyWeaponDefinition.json"

    f = open(weapon_file_name, "w", encoding="utf-8")
    hash_index = 0
    f.write('{')
    for weapon in weapon_list:
        f.write('"'+str(hash_list[hash_index])+'" :'+str(weapon)+', '+"\n")
        hash_index = hash_index + 1
    f.write('{')
    f.close()
    print("weapon file generated")
##    jsb.beautify_file(weapon_file_name)
##    print("weapon file formatted")

print()
print()

def GeneratePerkList():
    perk_list = []
    hash_list = []

    with open(file_name, "rb") as f:
        my_list = json.load(f)

        for idx, obj in my_list.items():
            if obj != None:
                if obj["itemType"] == 19 and obj["displayProperties"]["name"] != None:
                    if obj["itemTypeDisplayName"]=="Trait" or obj["itemTypeDisplayName"]=="Barrel" or obj["itemTypeDisplayName"]=="Magazine" or obj["itemTypeDisplayName"]=="Enchanced Trait":
                        perk_list.append(obj)
                        hash_list.append(obj["hash"])

    perk_file_name = "DestinyPerkDefinition.json"

    f = open(perk_file_name, "w", encoding="utf-8")
    hash_index = 0
    f.write('{')
    for perk in perk_list:
        f.write('"'+str(hash_list[hash_index])+'": '+str(perk)+', '+"\n")
        hash_index = hash_index + 1
    f.write('}')
    f.close()
    print("perk file generated")
##    jsb.beautify_file(perk_file_name)
##    print("perk file formatted")

def DeleteItemFile():
    os.remove(file_name)
    print("item file removed")
