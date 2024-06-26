from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    return HttpResponse('<h1>Good Morning.....</h1>')

def test1(request):
    return render(request,'test1.html')

