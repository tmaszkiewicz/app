from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def home(request, *arg, **kwargs):
    url = 'app/home.html'
    context = {
    }
    tekst = "dasdasd"

    context['tekst']=tekst 
    #return HttpResponse("LoveMonika")
    return render(request,url,context)
