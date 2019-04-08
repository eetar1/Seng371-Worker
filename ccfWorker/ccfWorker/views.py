import base64
import json
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
import os
from .invert import process
from .dataFetch import getAllImages
import io


@csrf_exempt
def workpage_view(request):

    if request.method == "POST":
        if request.COOKIES["psw"] == os.environ.get('worker_password'):
            by = ""
            img = getAllImages(request.COOKIES['url'])
            with open('tmpFile.jpg','wb+') as  fp:
                fp.write(img)

            out = process('tmpFile.jpg')
            os.remove('tmpFile.jpg')
            arr= io.BytesIO()
            out.save(arr,format=('JPEG'))
            out = arr.getvalue()
            by = base64.b64encode(out)

            data = {"path": os.getcwd(), "url": request.COOKIES["url"], "img": str(by)}
            return HttpResponse(json.dumps(data))

    else:
        return render(request, "tmp_home.html")
