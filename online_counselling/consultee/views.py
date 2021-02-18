from django.shortcuts import render, HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse('In Consultee')

def register_consultee(request):
	return HttpResponse('done')