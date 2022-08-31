# from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient

connection_string = "mongodb://localhost/yelpcamp_django"
client = MongoClient(connection_string)
db = client['yelpcamp_django']
locations_collection = db["locations"]

medicine_1 = {
    "medicine_id": "RR000123456",
    "common_name": "Paracetamol",
    "scientific_name": "",
    "available": "Y",
    "category": "fever"
}
medicine_2 = {
    "medicine_id": "RR000342522",
    "common_name": "Metformin",
    "scientific_name": "",
    "available": "Y",
    "category": "type 2 diabetes"
}


def campgrounds_list(request):
    # locations_collection.insert_many([medicine_1, medicine_2])
    return render(request, "campgrounds/index.html")
