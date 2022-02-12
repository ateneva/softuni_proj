from django.http import HttpResponse
from django.shortcuts import render
from demo_app.models import Task

# Create your views here.

# function-based views

# return values from the connected backend database
def home_page(request):
    tasks_list = Task.objects.all()
    context = {'tasks_list': tasks_list}
    if not context:
        context = "There are no created tasks!"

    return render(request, 'demo_app/index.html', context)

# class-based views