from django.urls import path
from . import views

app_name = 'campgrounds'

urlpatterns = [
    path("", views.campgrounds_list, name='list'),
]
