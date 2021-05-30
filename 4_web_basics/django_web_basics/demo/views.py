from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home_page(request):
	context = {
		'name': 'Angelina'
	}
	return render(request, 'index.html', context)
	# subdirectory within templates expected