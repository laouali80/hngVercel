from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.shortcuts import redirect

# Create your views here.

import os
from dotenv import load_dotenv

load_dotenv()

@api_view(['GET'])
def test(request):
    return Response(
        {"etrtr":"fgf"}
    )

# @api_view(['GET'])
# def welcome(request):
#     return redirect('api')




# @api_view(['GET'])
# def api(request):
#     visitor_name = request.GET.get('visitor_name', 'Mark')
    
#     # Get the IP address
#     ip_address_response = requests.get('http://api.ipify.org')
#     ip_address = ip_address_response.text
    
#     # Get the location data
#     location_response = requests.get(f'http://ip-api.com/json/{ip_address}')
#     location_data = location_response.json()
    
#     # Get the weather data
#     weather_response = requests.get(
#         f"https://api.openweathermap.org/data/2.5/weather?lat={location_data['lat']}&lon={location_data['lon']}&units=Metric&appid={os.getenv("api_key")}"
#     )
#     weather_data = weather_response.json()
    
#     data = {
#         "client_id": ip_address,
#         "location": location_data["city"],
#         "greeting": f"Hello, {visitor_name.title()}!,the temperature is {weather_data['main']['temp']} degrees Celsius in {location_data['city']}"
#     }
#     return Response(data)