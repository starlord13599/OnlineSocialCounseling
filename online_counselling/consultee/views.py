from django.shortcuts import render, HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse('In Consultee')