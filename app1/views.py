from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msg(request):
    return HttpResponse('<h1>moye moyee......')

def test2(request):
    return render(request,'test2.html')