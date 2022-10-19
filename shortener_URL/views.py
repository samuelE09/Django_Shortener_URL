from django.shortcuts import render

import pyshorteners

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def url_shortened(request):
    if request.GET.get('long_url') != '': 
        long_url = length = request.GET.get("long_url")
        service_tiny = pyshorteners.Shortener()
        short_url = service_tiny.tinyurl.short(long_url)
        return render(request, 'url_shortened.html' , {'short_url' : short_url})
    else: 
        short_url = "No se encontró una URL Válida"
        return render(request, 'url_shortened.html' , {'short_url' : short_url})