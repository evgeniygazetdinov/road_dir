from django.shortcuts import render
import random
from django.shortcuts import render


def generate_road():
    pass


def generate_cars():
    pass


def road_controller(request):
    road = generate_road()
    cars = generate_cars()
    return render(request, 'road/index.html' ,context = {'cars': cars, 'road': road})