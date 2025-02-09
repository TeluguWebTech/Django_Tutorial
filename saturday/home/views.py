from django.shortcuts import render
from .models import Home

# Create your views here.

def landing_page(request):

    home_items = Home.objects.all()
    return render(request, 'home.html', {'home_items':home_items})