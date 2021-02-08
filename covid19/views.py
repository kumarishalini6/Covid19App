from django.shortcuts import render
import requests
from rest_framework import filters
# Create your views here.


def index(request):
    result = requests.get('https://api.covid19api.com/summary')
    json = result.json()
    globalSummery = json['Global']
    countries = json['Countries']
    return render(request, 'index.html', {'globalSummery': globalSummery,
                                          'countries': countries})


