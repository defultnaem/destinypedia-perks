import json
import os

file_name = "DestinyInventoryItemDefinition.json"

def GenerateWeaponList():
    weapon_list = []
    name_list = []

    with open(file_name, "r", encoding="utf-8") as f:
        my_list = json.load(f)

        for idx, obj in my_list.items():
            if obj != None:
                if obj["itemType"] == 3:
                    weapon_list.append(obj)
                    name_list.append(obj["displayProperties"]["name"])
                    print(str(obj["hash"])+": "+obj["displayProperties"]["name"]+" added to weapon list")

    weapon_file_name = "DestinyWeaponDefinition.json"

    f = open(weapon_file_name, "w")
    name_index = 0
    for weapon in weapon_list:
        f.write('"'+str(name_list[name_index])+'": '+str(weapon)+"\n")
        name_index = name_index + 1
    f.close()
    print("weapon file generated")

print()
print()

def GeneratePerkList():
    perk_list = []
    hash_list = []

    with open(file_name, "r", encoding="utf-8") as f:
        my_list = json.load(f)

        for idx, obj in my_list.items():
            if obj != None:
                if obj["itemType"] == 19 and obj["displayProperties"]["name"] != None:
                    if obj["itemTypeDisplayName"] == "Trait":
                        perk_list.append(obj)
                        hash_list.append(obj["hash"])
                        print(str(obj["hash"])+": "+obj["displayProperties"]["name"]+" added to perk list")
                    if obj["itemTypeDisplayName"] == "Enhanced Trait":
                        perk_list.append(obj)
                        hash_list.append(obj["hash"])
                        print(str(obj["hash"])+": Enhanced "+obj["displayProperties"]["name"]+" added to perk list")

    perk_file_name = "DestinyPerkDefinition.json"

    f = open(perk_file_name, "w")
    hash_index = 0
    for perk in perk_list:
        f.write('"'+str(hash_list[hash_index])+'": '+str(perk)+"\n")
        hash_index = hash_index + 1
    f.close()
    print("perk file generated")

def DeleteItemFile():
    os.remove(file_name)
    print("item file removed")
