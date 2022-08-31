# from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient
from django import template
from bson.objectid import ObjectId

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
register = template.Library()


# @register.filter(name='get')
# def get(d, k):
#     return d.get(k, None)

def private(dic, key):
    print(key)
    return 'dic[key]'


def campgrounds_list(request):
    campgrounds = locations_collection.find({})
    mapped_campgrounds = list(
        map(lambda x: {'id': x['_id'], **x}, campgrounds))
    # locations_collection.insert_many([location_1, location_2])
    return render(request, "campgrounds/index.html", {'campgrounds': mapped_campgrounds, 'private': private})


def campground_detail(request, id):
    try:
        campground = locations_collection.find_one({'_id': ObjectId(id)})
    except NameError:
        raise Http404("Question does not exist")
    return render(request, 'campgrounds/campground_detail.html', {'campground': campground})
