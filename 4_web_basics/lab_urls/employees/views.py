from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
	return HttpResponse('The App works')


def department_list(request):
	return HttpResponse('This is department list page')


# create a dynamic view by using a parameter
def department_details(request, id):
	return HttpResponse(f'This is department {id} page')


