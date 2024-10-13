from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is homepage")
    
def importantdates(request):
    return render(request, 'importantdates.html')

def downloads(request):
    return render(request, 'downloads.html')

def faqs(request):
    return render(request, 'faqs.html')        

def contactus(request):
    return render(request, 'contactus.html')    