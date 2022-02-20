from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
# Create your views here.

# A function is a Django view if:
# * accepts HTTPrequest as a first parameter
# * returns an HTTPresponse

def home_page(request):
	html = f'<h1>{request.method}: The App works</h1>'
	return HttpResponse(
			html,
			#content_type = 'text/plain',
			headers={
				'x-annie-header': 'Django',
			},
		)

def department_list(request):
	return HttpResponse('This is department list page')


# create a dynamic view by using a parameter
def department_details(request, id):
	return HttpResponse(f'This is department {id} page')


# raise exceptions
def department_employees(request, department_id):
	employee = None

	if department_id > 0 and department_id < 3:
		if department_id == 1:
			employee = "Peter Smith"

		elif department_id == 2:
			employee = "Mariya Brown"

		html = "<html><body><h1>Employee: %s, " \
			   "Department: %s</h1></body></html>" \
			   % (employee, department_id)

		return HttpResponse(html)
	else:
		return HttpResponseNotFound('<h1>Department was not found</h1>')

	# return HTTPresponseNotFound('Department was not found')
		# is the same as
	# return HTTPresponse(status=404)
	# raise Http404


# use render fucntion to return an html template page
# context = an optional argument used to add dictionary values to a template
def employees_by_department(request):
	context = {
		"employee": "Peter Smith",
		"department": 'Marketing',
		"departments": ['Finance', 'Marketing', 'HR', 'Technology']
	}

	return render(
		request=request,
		template_name='deps.html',
		context=context
	)

# re-direct to home_page
def go_to_home(request):
	return redirect(to='/')
	#return HttpResponseRedirect()
