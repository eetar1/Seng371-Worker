import requests
from PIL import Image
import json
import base64

def postTest():
   
    url  = 'https://seng371worker.herokuapp.com/'
    data = {
        'url':"https://cbers-stac-0-6.s3.amazonaws.com/CBERS4/MUX/065/094/catalog.json",
        'intGit':"www.Ethan.com",
        'outGit':'www.Ross.com',
        'psw':r"""UoSH{&W-J2tA.KYV9c/#!6!MQ+-M/\~[<dhJNQ22>ny}$-Tpj"H%NQ'eq\'fo88[L]n1)5<H5~WO_/j#|t|@5!p[}pp:#Gn8%g.P"""
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