import requests
from PIL import Image
import json
import base64
def postTest():
   
    url  = 'http://127.0.0.1:8000/'
    data = {
        'url':"WWW.prawn.com",
        'intGit':"www.Ethan.com",
        'outGit':'www.Ross.com'
    }
    req = requests.post(url,cookies=data)
    jos = json.loads(req.text)
    by  = jos['img']
    by = by[2:-1]
    by = base64.b64decode(by)
    with open("file.jpg",'wb') as fp:
        fp.write(by)
    img = Image.open("file.jpg")
    img.show()
   



def main():
    postTest()



if __name__ == "__main__":
    main()