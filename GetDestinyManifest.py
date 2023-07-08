def GetDestiny2EnManifestPath():
    import requests
    import json
    url = "https://www.bungie.net/Platform/Destiny2/Manifest"
    payload = {}
    headers = {
      'x-api-key': 'b51473b6521d458b8733d0844cd66f1f',
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    manifest = json.loads(response.content)
    enManifestPath = manifest["Response"]["mobileWorldContentPaths"]["en"]
    enManifestPath = "https://bungie.net"+enManifestPath

    print(enManifestPath)

GetDestiny2EnManifestPath()
