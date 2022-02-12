### create a virtual environment
```bash
python3 -m venv django_venv
source django_venv/bin/activate
```

### install django
```bash
python3 -m pip install django
python3 -m django --version
```
https://docs.djangoproject.com/en/4.0/topics/install/


### start a django project
```bash
django-admin startproject mydjangosite
```

### django project structure
![](../../../../../../var/folders/dp/ylq2fsb959qdhsb_jb2ds9d00000gr/T/TemporaryItems/NSIRD_screencaptureui_5efxww/Screenshot 2022-02-12 at 12.48.54.png)
* `settings.py` - configuration file for the project
* `urls.py` - holds the contents of the project
* `manage.py` - executes commands for the project

### verify that your django project works
```bash
cd mydjangosite
python manage.py runserver
```

### create a new app
```bash
python manage.py startapp demo

# OR  
django-admin startapp main_app
django-admin startapp secondary_app
```

### update settings installed apps
```python
# Application definition

INSTALLED_APPS = [
    'demo.apps.DemoConfig',
    'main_app',
    'secondary_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### update views.py
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return render(request, 'index.html')
	# subdirectory within templates expected
```


### create urls.py in the app directory
```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name= 'demo-home'),
]
```

### update urls.py in the project directory to point to the app urls
```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo.urls')),
]
```