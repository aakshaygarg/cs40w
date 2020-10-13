from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def greet(request, name):
    index="hello/index.html"
    return render(request, index, {
        "name": name.capitalize()
    })
