import os
import sys

import PIL.ImageOps
from PIL import Image


def process(img):
    image = Image.open(img)
    out = PIL.ImageOps.invert(image)
    return out


def main():
    name = sys.argv[1:]
    process(name)


if __name__ == "__main__":
    main()
