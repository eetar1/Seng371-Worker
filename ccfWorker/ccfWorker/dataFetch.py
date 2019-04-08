import requests
import io
from PIL import Image 
import os
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
    s = "https://cbers-stac-0-6.s3.amazonaws.com/CBERS4/MUX/065/094/catalog.json"
    img = getAllImages(s)
    with open("file.jpg","wb+") as fp:
        fp.write(img)
    img = Image.open("file.jpg")
    img.show()
    os.remove("file.jpg")




if __name__ == "__main__":
    main()

