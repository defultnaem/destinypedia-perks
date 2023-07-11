import json
import os

def GenerateWeaponList():
    file_name = "DestinyInventoryItemDefinition.json"
    weapon_list = []
    hash_list = []

    with open(file_name, "r", encoding="utf-8") as f:
        my_list = json.load(f)

        for idx, obj in my_list.items():
            if obj != None:
                if obj["itemType"] == 3:
                    weapon_list.append(obj)
                    hash_list.append(obj["hash"])
                    print(str(obj["hash"])+": "+obj["displayProperties"]["name"]+" added")

    new_file_name = "DestinyWeaponDefinition.json"

    f = open(new_file_name, "w")
    hash_index = 0
    for weapon in weapon_list:
        f.write("'"+str(hash_list[hash_index])+"': "+str(weapon)+"\n")
        hash_index = hash_index + 1
    f.close()
    print("weapon file generated")

    os.remove(file_name)
    print("item file removed")
