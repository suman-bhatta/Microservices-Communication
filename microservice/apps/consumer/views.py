from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['POST'])
def receive_message(request):
    data = request.data
    print(f"Received message: {data}")  # Process the message
    return Response({"status": "Message received", "data": data})
