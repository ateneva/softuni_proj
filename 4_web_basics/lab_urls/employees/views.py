from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# A function is a Django view if:
# * accepts HTTPrequest as a first parameter
# * returns an HTTPresponse

def home_page(request):
	html = f'<h1>{request.method}: The App works</h1>'
	return HttpResponse(html)


def department_list(request):
	return HttpResponse('This is department list page')


# create a dynamic view by using a parameter
def department_details(request, id):
	return HttpResponse(f'This is department {id} page')
