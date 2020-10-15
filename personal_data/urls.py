from django.urls import path
from . import views

app_name = 'personal_data'
urlpatterns =[
    path('create', views.Registration.create),
    path('edit', views.Registration.edit),
    path('delete', views.Registration.delete),
    path('',views.show),
]