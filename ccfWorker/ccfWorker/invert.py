import os
import sys

import PIL.ImageOps
from PIL import Image


def process(name):
    image = Image.open(str(name[0]))
    out = PIL.ImageOps.invert(image)
    out.save(os.getcwd() + "/ccfWorker/ccfWorker/fixed.jpg")


def main():
    name = sys.argv[1:]
    process(name)


if __name__ == "__main__":
    main()
