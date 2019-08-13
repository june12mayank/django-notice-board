from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myView(request):
	return HttpResponse('Shingeki no Kyojin <br> one punch man <br><b> Naruto</b>')