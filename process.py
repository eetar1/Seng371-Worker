import PIL.ImageOps
from PIL import Image


def process():
    img = Image.open("Img.jpeg")
    out = PIL.ImageOps.invert(img)
    out.save("Img.jpg")
    '''
    with open("Img.jpg","wb+") as fp:
        fp.write(img)
        '''
