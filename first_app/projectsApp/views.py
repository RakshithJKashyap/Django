from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def projects(request):
    msg = "hello u r on the projects page"
    age = 12
    context = {'m':msg,'age':age} 
    return render(request, 'projects.html',context)

