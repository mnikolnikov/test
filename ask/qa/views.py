from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

def test(request, *args, **kwargs):
    return HttpResponse('OK')
def popular(request, *args, **kwargs):
	try:
		pass
	except Exception, e:
		raise Http404
# Create your views here.
