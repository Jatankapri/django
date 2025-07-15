from django.shortcuts import render
def category_home(request):
    return render(request, 'categories/category_home.html'
                  
                  )
# Create your views here.
from django.urls import path
from . import views
urlpatterns = [
    path('', views.category_home, name='category_home'),
]