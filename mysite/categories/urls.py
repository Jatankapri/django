from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.category_home, name='category_home'),
]
   
        