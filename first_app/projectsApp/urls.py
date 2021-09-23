from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.projects,name="Hello"),
    path('projects/<str:pk>/',views.products,name="Products")
    
]

