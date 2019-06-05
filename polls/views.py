from django.http import HttpResponse
from django.shortcuts import render


'''
XSS Vulnerabilites in hello API
'''
def xss(request):
	id=request.GET.get('id')
	return HttpResponse("Hello %s" % id)

def antixss(request):
	id=request.GET.get('id')
	return render(request,"antixss.html",{'id':id})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")