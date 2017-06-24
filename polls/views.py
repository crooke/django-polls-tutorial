from django.shortcuts import render

def index(request):
	return HttpResponse("Hello, world! Welcome to the Polls app")