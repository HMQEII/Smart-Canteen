from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.home, name='home'),
    path('Login/', views.login, name='login'),
    path('Home/Veg/', views.Veg, name='veg'),
    path('Home/NonVeg/', views.NVeg, name='nveg'),
]