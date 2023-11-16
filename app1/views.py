from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rcb(request):
  return render(request,'sreenu.html')

def kohil(request):
  return HttpResponse('<h1><b>kohil is best batsman in the world</b></h2>')
  
