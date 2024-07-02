from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# Create your views here.


@api_view(['GET'])
def test(request):
    test = {
        'dcijsf':'test',
    }
    return Response(test)