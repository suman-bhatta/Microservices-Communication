from django.urls import path
from .views import send_message

urlpatterns = [
    path('send/', send_message, name='send_message'),
]
