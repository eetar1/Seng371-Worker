import base64
import json
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
import os
from .invert import process
import io


@csrf_exempt
def workpage_view(request):

    """
    request.COOKIES['url'] get url of cookie
    """

    if request.method == "POST":
        if request.COOKIES["psw"] == os.environ.get('worker_password'):
            by = ""
            out = process([os.getcwd() + "/ccfWorker/ccfWorker/testImage.jpg"])
            arr= io.BytesIO()
            out.save(arr,format=('JPEG'))
            out = arr.getvalue()
            by = base64.b64encode(out)

            data = {"path": os.getcwd(), "url": request.COOKIES["url"], "img": str(by)}
            return HttpResponse(json.dumps(data))

    else:
        return render(request, "tmp_home.html")
