from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.projects,name="Hello"),
    path('projects/<str:pk>/',views.products,name="Products"),
    path('create/',views.create_project,name="createProject"),
    path('update/<str:pk>',views.update_project,name="updateProject")
]

