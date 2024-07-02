from rest_framework.decorators import api_view
from rest_framework.response import Response
import httpx

# Create your views here.


@api_view(['GET'])
def welcome(request):
    test = {
        'dcijsf':'test',
    }
    return Response(test)

@api_view(['GET'])
async def api(request):
    visitor_name = request.GET.get("visitor_name", "mark")
    async with httpx.AsyncClient() as client:
        ipAddress = await client.get('http://api.ipify.org')
        response = await client.get(f'http://ip-api.com/json/{ipAddress}').json()
        temp = await client.get(f"https://api.openweathermap.org/data/2.5/weather?lat={response['lat']}&lon={response['lon']}&units=Metric&appid=bb7a48fca8cf8f19e33795a6d147c742")
    return {
        "client_id": ipAddress,
        "location": response["city"],
        "greeting": f"Hello, {visitor_name.title()}!, the temperature is {temp["main"]["temp"]} degrees Celcius in {response["city"]}"
    }