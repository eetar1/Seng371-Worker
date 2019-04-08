import requests

# Input: url to STAC catalog
# Output: the list of urls to STAC items in the catalog
def getSTACItemsFromCatalog(catalog):
    resp = requests.get(catalog).json()["links"]
    url = catalog.split("catalog.json")[0]

    items = []
    for elem in resp:
        if elem["rel"] != "item":
            continue
        items.append(url + elem["href"])
    return items


# Input: url to STAC item
# Output: the url to the image
def getImageURLFromSTACItem(item):
    return requests.get(item).json()["assets"]["thumbnail"]["href"]


# Used for testing purposes
def main():
    s = "https://cbers-stac-0-6.s3.amazonaws.com/CBERS4/MUX/065/094/catalog.json"
    items = getSTACItemsFromCatalog(s)
    for i in items:
        print(i)
    print(getImageURLFromSTACItem(items[0]))


if __name__ == "__main__":
    main()

