import json

ItemDefinition = "DestinyInventoryItemDefinition.json"
PlugSetDefinition = "DestinyPlugSetDefinition.json"
perks_indexes = []

with open(PlugSetDefinition, "rb") as plugsets:
    plugset_list = json.load(plugsets)
    plugset_list = plugset_list.items()
    print(len(plugset_list))

with open(ItemDefinition, "rb") as items:
    item_list = json.load(items)

    for iidx, iobj in item_list.items():
        if iobj != None:
            if iobj["itemType"] == 3:
                if iobj["hash"] == 2856514843:
                    print("item index - "+str(iidx))
                    # checking for socket category 4241085061 (WEAPON PERKS) #
                    for socketCategory in iobj["sockets"]["socketCategories"]:
                        socketCategoryHash = socketCategory["socketCategoryHash"]
                        if socketCategoryHash == 4241085061:
                            print("socket category - "+str(socketCategory))
                            for socketIndex in socketCategory["socketIndexes"]:
                                if iobj["sockets"]["socketEntries"][socketIndex]["socketTypeHash"] != 1282012138:
                                    print("socket index - "+str(socketIndex))
                                    for pidx, pobj in item_list.items():
                                        if pobj != None:
                                            if pobj["itemType"] == 19 and pobj["displayProperties"]["name"] != None:
                                                if iobj["sockets"]["socketEntries"][socketIndex]["singleInitialItemHash"] == pobj["hash"]:
                                                    print("perk index - "+str(pidx))
                                                    print(pobj["displayProperties"]["name"])
                                                    print(iobj["sockets"]["socketEntries"][socketIndex]["singleInitialItemHash"])
                                    
##                                        if plugset_list["hash"] == 2044988252:
##                                            for plugItem in plugset_list["reusablePlugItems"]:
##                                                print("plug set index - "+str(psidx))
##                                                    if iobj["sockets"]["socketEntries"][socketIndex]["randomizedPlugSetHash"] == psobj["hash"] and psobj["hash"] == 2044988252:
##                                                            for plugItem in psobj["reusablePlugItems"]:
##                                                                print(plugItem["plugItemHash"])



                                                
                                                
                        # checking socket entries for slots matching 4241085061 indexes#
##                        print(len(obj["sockets"]["socketEntries"]))
##                        for entries in obj["sockets"]:
##                            print(entries)
