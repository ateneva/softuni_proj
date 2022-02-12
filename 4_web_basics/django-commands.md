
### general syntax
```bash
$ django-admin <command> [options]
$ manage.py <command> [options]
$ python -m django <command> [options]
```
* Any django command can be run with either of the 3 options
* Generally, when working on a single Django project, it’s easier to use manage.py than django-admin

### django admin
```bash
django-admin help --commands  # list all available django-admin-commands
django-admin help --command   # show help for a particular command
django-admin version          # display the djangpo version

django-admin runserver
django-admin startapp <app_name>
```

### manage.py
```bash
python manage.py version
python manage.py help
python manage.py runserver
python manage.py startapp <app_name>
python manage.py makemigrations         # create migrations for the added model;
python manage.py migrate                # apply migrations to your project
python manage.py inspectdb > models.py  # integrate django with existing DB & generate a models file
python manage.py createsuperuser        # create super user for the django admin
```

### python -m django
```bash
python -m django version
python -m django help
python -m django help --<command>
python -m django runserver
python -m django startapp <app_name>
```

https://docs.djangoproject.com/en/4.0/ref/django-admin/
https://docs.djangoproject.com/en/4.0/howto/legacy-databases/


