from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from django.urls import path
from canteen.views import scan_barcode
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('scan_barcode/', scan_barcode, name='scan_barcode'),
#     # Other URL patterns...
# ]


urlpatterns = [
    path('', RedirectView.as_view(url='/Login/')),
    path('Home/', views.home, name='home'),
    path('Wallet/', views.Wallet, name='wallet'),
    path('Login/', views.login, name='login'),
    path('Home/Veg/', views.Veg, name='veg'),
    path('Home/NonVeg/', views.NVeg, name='nveg'),
    path('Home/checkout.html', views.checkout, name='checkout'),
    path('Home/Beverage/', views.Beverage, name='beverage'),
    path('predicted-demand/', views.sales_prediction_view, name='predicted_demand'),
    path('suggest_order/', views.suggest_order, name='suggest_order'),
    path('checkout/', views.checkout, name='checkout'),
    # path('addtocart/', views.addtocart, name='addtocart'),
    path('addtocart/', views.addtocart, name='addtocart'),
]