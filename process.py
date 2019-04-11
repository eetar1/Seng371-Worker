import PIL.ImageOps
from PIL import Image


def process(filename):
    img = Image.open(filename)
    out = PIL.ImageOps.invert(img)
    out.save(filename)
    """
    with open(filename,"wb+") as fp:
        fp.write(img)
        """
