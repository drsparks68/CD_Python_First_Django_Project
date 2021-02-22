from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return HttpResponseRedirect("/")

def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit plog {num}")

def destroy(request, num):
    return HttpResponseRedirect("/")

