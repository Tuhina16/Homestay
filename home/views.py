from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/index.html')
    # return HttpResponse("This is Homepage")

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'accounts/register.html')
    # return HttpResponse("This is About page")

def details(request):
    return render(request, 'details.html')