import requests
import sys
from process import process


# Input: url to STAC item
# Output: the url to the preview image
def get_image_URL_from_STAC_item(item):
    return requests.get(item).json()["assets"]["thumbnail"]["href"]

# Used for testing purposes
def main():
    url = sys.argv[1]
    url = get_image_URL_from_STAC_item(url)

    img = requests.get(url)
    img = img.content

    filename = sys.argv[2] + ".jpeg"
    with open(filename,"wb+") as fp:
        fp.write(img)
    process(filename)
        
if __name__ == "__main__":
    main()

