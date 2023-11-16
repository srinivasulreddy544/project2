from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reddy(request):
  return render(request,'kohil.html')
def abd(request):
  return HttpResponse('<h1>MR.360</h1>')