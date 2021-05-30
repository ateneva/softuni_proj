
### start a django project
```
django-admin startproject mydjangosite
```

### verify that your django project works
```
cd mydjangosite
python manage.py runserver
```

### create a new app
```
python manage.py startapp demo

# OR  
django-admin startapp main_app
django-admin startapp secondary_app
```

###update settings installed apps
```
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
```
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return render(request, 'index.html')
	# subdirectory within templates expected

create urls.py in the app directory
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name= 'demo-home'),
]
```

### update urls.py in the project directory to point to the app urls

```
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo.urls')),
]
```
