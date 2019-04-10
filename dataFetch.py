import requests
from PIL import Image 
import sys
from process import process

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
    url = sys.argv[1]
   # url = getSTACItemsFromCatalog(url)
    url = getImageURLFromSTACItem(url)
    img = requests.get(url)
    img = img.content
    with open("Img.jpeg","wb+") as fp:
        fp.write(img)
    process()
        
if __name__ == "__main__":
    main()

