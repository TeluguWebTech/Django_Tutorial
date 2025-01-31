
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def About_Page(request):
    return HttpResponse("Hello World !")


def shopping_page(request):
    data = {"city": "Hyderabad"}
    return JsonResponse(data)

# html page


def showing_html(request):
    return render(request, "home.html")


def story_page(request):
    return render(request, "story.html")
