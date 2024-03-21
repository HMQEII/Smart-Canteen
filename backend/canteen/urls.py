from django.urls import path
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='/Login/')),
    path('Home/', views.home, name='home'),
    
    path('Login/', views.login, name='login'),
    path('Home/Veg/', views.Veg, name='veg'),
    path('Home/NonVeg/', views.NVeg, name='nveg'),
    path('predicted-demand/', views.sales_prediction_view, name='predicted_demand'),
    path('suggest_order/', views.suggest_order, name='suggest_order'),
]