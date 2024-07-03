import requests
from django.shortcuts import redirect, reverse

from django.http import JsonResponse

# Create your views here.

import os
from dotenv import load_dotenv

load_dotenv()



def welcome(request):
    return redirect(reverse('api') + '?visitor_name=mark')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def api(request):
    visitor_name = request.GET.get('visitor_name', 'Mark')
    
    client_ip = get_client_ip(request)
    
    locat_resp = requests.get(f'http://ip-api.com/json/{client_ip}')
    location_data = locat_resp.json()

    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_data['lat']}&lon={location_data['lon']}&units=Metric&appid={os.getenv("api_key")}")
    weather_data = weather_resp.json()
    
    data = {
        "client_ip": client_ip,
        "location": location_data["city"],
        "greeting": f"Hello, {visitor_name.title()}!,the temperature is {weather_data['main']['temp']} degrees Celsius in {location_data['city']}"
    }
    return JsonResponse(data, status=200)
