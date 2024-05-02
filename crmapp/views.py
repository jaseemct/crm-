from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def dash(request):
    return render(request,'dashbord.html')

def archive(request):
    return render(request,'archive.html')
