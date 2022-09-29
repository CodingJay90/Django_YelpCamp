from django.urls import path
from . import views

app_name = 'campgrounds'

urlpatterns = [
    path("", views.campgrounds_list, name='home'),
    path('add/', views.campground_add, name='add'),
    path('<str:id>/', views.campground_detail, name='detail'),
    path('edit/<str:id>/', views.campground_edit, name='edit'),
    path('delete/<str:id>/', views.campground_delete, name='delete'),
]
