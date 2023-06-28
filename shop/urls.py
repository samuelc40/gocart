from django.urls import path
from . import views
from cart import views as view

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:c_slug>/', views.catview, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodetails, name='details'),
    path('search', views.searching, name='search'),
    path('cartdetails', view.cart_details, name='cartdetails'),
    path('checkout', view.checkout, name='checkout')
]