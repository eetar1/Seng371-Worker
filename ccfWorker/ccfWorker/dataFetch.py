import requests
import io
from PIL import Image 
import os
import sys
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

def getAllImages(url):
    items = getSTACItemsFromCatalog(url)
    urls = []
    #for link in items:
    urls.append(getImageURLFromSTACItem(items[0]))
    img = requests.get(urls[0])
    return img.content


# Used for testing purposes
def main():
    url = sys.argv[1]
    cnt = 1
    url = getImageURLFromSTACItem(url)
    img = requests.get(url)
    img = img.content
    with open("Image.jpeg","wb+") as fp:
        fp.write(img)
        







if __name__ == "__main__":
    main()

