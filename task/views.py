from rest_framework.decorators import api_view
from rest_framework.response import Response
import httpx

# Create your views here.

import os
from dotenv import load_dotenv

load_dotenv()



@api_view(['GET'])
def welcome(request):
    test = {
        'dcijsf':'test',
    }
    return Response(test)


@api_view(['GET'])
async def test(request):
    visitor_name = request.query_params.get('visitor_name', 'Mark')
    
    async with httpx.AsyncClient() as client:
        ip_address_response = await client.get('http://api.ipify.org')
        ip_address = ip_address_response.text
        
        location_response = await client.get(f'http://ip-api.com/json/{ip_address}')
        location_data = location_response.json()
        
        weather_response = await client.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={location_data['lat']}&lon={location_data['lon']}&units=Metric&appid={os.getenv('api_key')}"
        )
        weather_data = weather_response.json()
    
    return Response({
        "client_id": ip_address,
        "location": location_data["city"],
        "greeting": f"Hello, {visitor_name.title()}!, the temperature is {weather_data['main']['temp']} degrees Celsius in {location_data['city']}"
    })
