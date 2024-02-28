from django.urls import path
from .views import greetings,encode

urlpatterns=[
    path('',greetings),
    path('ceaser/<str:plaintext>/<int:shift>',encode),
]