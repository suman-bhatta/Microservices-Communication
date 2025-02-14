from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


CONSUMER_API_URL = "http://127.0.0.1:8001/consumer/receive/"  # Consumer API endpoint

@api_view(['POST'])
def send_message(request):
    data = request.data
    try:
        response = requests.post(CONSUMER_API_URL, json=data)
        return Response({"status": "Message sent", "consumer_response": response.json()})
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)
