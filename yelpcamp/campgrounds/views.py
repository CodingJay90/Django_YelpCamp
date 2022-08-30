# from django.http import HttpResponse
from django.shortcuts import render


def campgrounds_list(request):
    return render(request, "campgrounds/index.html")
