from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This URL will be mapped to the home view
]
