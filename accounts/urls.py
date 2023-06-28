from django.urls import path
from . import views
from shop import views as view

urlpatterns = [
    path('home/', view.home, name='home'),
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]