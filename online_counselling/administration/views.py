from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	if request.method == 'GET':
		return render(request,'register.html')