from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .invert import process
import json
import os
import base64



@csrf_exempt
def workpage_view(request):

    '''
    request.COOKIES['url'] get url of cookie
    '''

    if request.method == 'POST':
        by = ''
        process([os.getcwd()+'/ccfWorker/testImage.jpg'])
        with open(os.getcwd()+'/ccfWorker/fixed.jpg',"rb") as fp:
            by = base64.b64encode(fp.read())
        
        data = {'path':os.getcwd(),'url':request.COOKIES['url'],'img':str(by)}
        os.remove(os.getcwd()+'/ccfWorker/fixed.jpg')
        return HttpResponse(json.dumps(data))
    else:
        return render(request, "tmp_home.html")