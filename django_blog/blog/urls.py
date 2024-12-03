from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This URL will be mapped to the home view
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
