from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def sayHello(request):
#     return HttpResponse('<h1 style="color:red">Hello World!! Learn django </h1>')

def sayHello(request):
    print('Request for sayHello page received')
    return render(request, 'index.html')