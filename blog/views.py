from django.http.response import HttpResponseBase
from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return render(request, "index.html", {'active':'active'})

def about(request):
    return render(request, 'about.html', {'active':'active'})

def contact(request):
    return render(request, 'contact.html', {'active':'active'})

def post(request):
    return render(request, 'post.html', {'active':'active'})