import json

ItemDefinition = "DestinyInventoryItemDefinition.json"
PlugSetDefinition = "DestinyPlugSetDefinition.json"
perks_indexes = []

global plugset_hashes
plugset_hashes = []

print()

def GetWeaponPerks(weaponHash):
    plugset_hashes = []
    with open(ItemDefinition, "rb") as items:
        item_list = json.load(items)

        for iidx, iobj in item_list.items():
            if iobj != None:
                if iobj["itemType"] == 3:
                    if iobj["hash"] == weaponHash:
                        print(iobj["displayProperties"]["name"])
                        print()
##                        print("item index - "+str(iidx))
                        for socketCategory in iobj["sockets"]["socketCategories"]:
                            socketCategoryHash = socketCategory["socketCategoryHash"]
                            if socketCategoryHash == 4241085061: # WEAPON PERKS
##                                print("socket category - "+str(socketCategory))
                                for socketIndex in socketCategory["socketIndexes"]:
                                    iobjSockets = iobj["sockets"]["socketEntries"][socketIndex]["socketTypeHash"]
                                    if "randomizedPlugSetHash" in iobj["sockets"]["socketEntries"][socketIndex]:
                                        iobjSockets_whitelist = [3362409147, 3815406785, 1215804697, 2575784089, 2614797986, 514622187, 1656112293, 4246926293, 2614797986]
                                        if iobj["summaryItemHash"] == 3520001075 or iobjSockets in iobjSockets_whitelist:
##                                            print("socket index - "+str(socketIndex))
                                            for pidx, pobj in item_list.items():
                                                if pobj != None:
                                                    if pobj["itemType"] == 19 or pobj["itemType"] == 20 or pobj["displayProperties"]["name"] != None:
                                                        if iobj["sockets"]["socketEntries"][socketIndex]["singleInitialItemHash"] == pobj["hash"]:
    ##                                                        print("perk index - "+str(pidx))
    ##                                                        print(pobj["displayProperties"]["name"])
    ##                                                        print(iobj["sockets"]["socketEntries"][socketIndex]["singleInitialItemHash"])
                                                            plugset_hashes.append(iobj["sockets"]["socketEntries"][socketIndex]["randomizedPlugSetHash"])
                                                            break
                                    elif "reusablePlugSetHash" in iobj["sockets"]["socketEntries"][socketIndex]:
                                        socketTypeHash = iobj["sockets"]["socketEntries"][socketIndex]["socketTypeHash"]
                                        socketTypeHash_whitelist = [3993098925, 3815406785, 3815406785, 3362409147, 514622187, 1656112293, 4246926293, 2614797986]
                                        if socketTypeHash in socketTypeHash_whitelist or iobj["summaryItemHash"] == 2673424576:
##                                            print("socket index - "+str(socketIndex))
                                            for pidx, pobj in item_list.items():
                                                if pobj != None:
                                                    if pobj["itemType"] == 19 or pobj["itemType"] == 20 or pobj["displayProperties"]["name"] != None:
                                                        if iobj["sockets"]["socketEntries"][socketIndex]["singleInitialItemHash"] == pobj["hash"]:
    ##                                                        print("perk index - "+str(pidx))
    ##                                                        print(pobj["displayProperties"]["name"])
    ##                                                        print(iobj["sockets"]["socketEntries"][socketIndex]["singleInitialItemHash"])
                                                            plugset_hashes.append(iobj["sockets"]["socketEntries"][socketIndex]["reusablePlugSetHash"])

##    print(plugset_hashes)
##    print()
    
    with open(PlugSetDefinition, "rb") as plugsets:
        plugset_list = json.load(plugsets)

        for psidx, psobj in plugset_list.items():
            if psobj != None:
                if psobj["reusablePlugItems"] != None:
                    if plugset_hashes.count(psobj["hash"]) > 0:
##                        print("plugset hash - "+str(psobj["hash"]))
                        plugSetPos = 0
                        for plugItem in psobj["reusablePlugItems"]:
                            for peidx, peobj in item_list.items():
                                if "itemTypeAndTierDisplayName" in peobj:
                                    displayType = peobj["itemTypeDisplayName"]
                                    displayType_whitelist = ["Trait", "Origin Trait", "Barrel", "Magazine", "Grip", "Guard", "Blade", "Launcher Barrel"]
                                    if displayType in displayType_whitelist:
                                        if psobj["reusablePlugItems"][plugSetPos]["plugItemHash"] == peobj["hash"]:
                                            print(peobj["displayProperties"]["name"])
##                            print(psobj["reusablePlugItems"][plugSetPos]["plugItemHash"])
                            plugSetPos = plugSetPos +1
                        print()
                                    
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
