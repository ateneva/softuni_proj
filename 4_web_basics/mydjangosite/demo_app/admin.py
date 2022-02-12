from django.contrib import admin
from demo_app.models import Task

# Register your models here to display them on the admin page
#admin.site.register(Task)


# Option 2: preferred as allows to customize the default view of the admin page
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_filter = ('title',)
    sortable_by = ('title', )