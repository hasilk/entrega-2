from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name="contact"),

    # Paths del admin
    
]
