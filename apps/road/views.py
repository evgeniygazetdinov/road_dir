from django.shortcuts import render
import random
from django.shortcuts import render


def generate_road():
    pass

def road_controller(request):
    context = {}
    road = generate_road()
    return render(request, 'road/index.html' ,context)