from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
]