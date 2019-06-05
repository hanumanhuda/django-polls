from django.http import HttpResponse




def hello(request):
	id=request.GET.get('id')
	return HttpResponse("Hello %s" % id)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")