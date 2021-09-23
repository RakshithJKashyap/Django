from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    msg = "hello u r on the projects page"
    age = 10
    context = {'m':msg,'age':age,'projects':projectsList} 
    return render(request, 'projects.html',context)



def products(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request,'product.html',{'project':projectObj})