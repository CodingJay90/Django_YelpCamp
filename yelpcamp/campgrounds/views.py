# from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymongo import MongoClient
from django import template
from bson.objectid import ObjectId
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

connection_string = "mongodb://localhost/yelpcamp_django"
client = MongoClient(connection_string)
db = client['yelpcamp_django']
locations_collection = db["locations"]

location_1 = {
    'name': 'Wolf creek',
    'image': 'https://images.unsplash.com/photo-1493612276216-ee3925520721?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80',
    'description': 'some long lorem ipsum text imagine it is',
    'cost': 10.99,
    'author': {
        'id': 2,
        'username': 'jay'
    },
    'location': 'California',
}
location_2 = {
    'name': 'Voldemort',
    'image': 'https://images.unsplash.com/photo-1493612276216-ee3925520721?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80',
    'description': 'some long lorem ipsum text imagine it is in Voldemort',
    'cost': 15.99,
    'author': {
        'id': 2,
        'username': 'jay'
    },
    'location': 'Tasmania',
}


def campgrounds_list(request):
    campgrounds = locations_collection.find({})
    mapped_campgrounds = list(
        map(lambda x: {'id': x['_id'], **x}, campgrounds))
    # locations_collection.insert_many([location_1, location_2])
    return render(request, "campgrounds/index.html", {'campgrounds': mapped_campgrounds})


def campground_detail(request, id):
    try:
        campground = locations_collection.find_one({'_id': ObjectId(id)})
        campground['id'] = campground['_id']
    except NameError:
        raise Http404("Question does not exist")
    return render(request, 'campgrounds/campground_detail.html', {'campground': campground})


def campground_edit(request, id):
    print(request.method)
    try:
        campground = locations_collection.find_one({'_id': ObjectId(id)})
        campground['id'] = campground['_id']
    except NameError:
        raise Http404("Question does not exist")

    if request.method == "POST":
        update_body = {
            'name': request.POST['name'],
            'image': request.POST['image'],
            'description': request.POST['description'],
            'cost': request.POST['cost'],
            'location': request.POST['name'],
        }
        locations_collection.update_one(
            {'_id': ObjectId(id)}, {"$set": update_body})
        return redirect("campgrounds:detail", id=id)
    return render(request, 'campgrounds/campground_edit.html', {'campground': campground})


def campground_delete(request, id):
    if request.method == 'POST':
        locations_collection.delete_one({'_id': ObjectId(id)})
        return redirect('campgrounds:home')


@login_required(login_url="/accounts/login/")
def campground_add(request):
    if request.method == 'POST':
        update_body = {
            'name': request.POST['name'],
            'image': request.POST['image'],
            'description': request.POST['description'],
            'cost': request.POST['cost'],
            'location': request.POST['name'],
            'author': {
                'id': request.user.id,
                'username': request.user.username
            },
        }
        result = locations_collection.insert_one(update_body)
        return redirect("campgrounds:detail", id=result.inserted_id)
    return render(request, "campgrounds/add_campground.html")
