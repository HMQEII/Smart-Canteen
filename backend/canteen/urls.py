from django.urls import path
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='/Login/')),
    path('Home/', views.home, name='home'),
    path('Login/', views.login, name='login'),
    path('Home/Veg/', views.Veg, name='veg'),
    path('Home/NonVeg/', views.NVeg, name='nveg'),
]