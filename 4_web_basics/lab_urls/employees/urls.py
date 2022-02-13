from django.urls import path, include
from employees import views

# Mandatory tuple or list
urlpatterns = [
    # path('department/', views.department, name='department'),   # localhost:8000/department
    # whether or not paths should be defined with an ending slash is defined in SETTINGS with the APPEND_SLASH
    path('', views.department_list),
    path('/<int:id>', views.department_details),


    # instead of writing departments multiple times in here, it's better to include it as a prefix in the project urls
    # path('departments/create', views.create_department),
    # path('departments/update', views.update_department),
    # path('departments/delete', views.delete_department),
]


