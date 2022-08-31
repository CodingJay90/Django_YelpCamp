from django.urls import path
from . import views

app_name = 'campgrounds'

urlpatterns = [
    path("", views.campgrounds_list, name='home'),
    path('<str:id>/', views.campground_detail, name='detail')
]
