from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    # return HttpResponse("<h1>Home page</h1>")
    return render(request, "store/index.html")
    # return render(request, response)