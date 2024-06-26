from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bye(request):
    return HttpResponse('<h1>Array is a collection of heterogeneous elements</h1>')

def test3(request):
    return render(request,'test3.html')
