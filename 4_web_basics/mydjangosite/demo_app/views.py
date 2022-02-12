from django.http import HttpResponse
from django.shortcuts import render
from demo_app.models import Task

# Create your views here.

# function-based views

# return values from the connected backend database
def home_page(request):
    tasks_list = Task.objects.all()
    output = "; ".join(f"{t.title}: {t.text}"
                       for t in tasks_list)
    if not output:
        output = "There are no created tasks!"

    return HttpResponse(output)

# class-based views