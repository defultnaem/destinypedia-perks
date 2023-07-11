import json

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

new_file_name = "DestinyWeaponDefinition.json"

f = open(new_file_name, "w")
for weapon in weapon_list:
    f.write(str(weapon)+"\n")
f.close()
