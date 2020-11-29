from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def mateusz(request):
    return HttpResponse("Hello Mateusz!!!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name}!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()        
    })