from django.shortcuts import render,redirect

from .models import project
from .forms import projectForm



# Create your views here.

def projects(request):
    projects = project.objects.all()
    
    context = {'projects':projects} 
    return render(request, 'projects.html',context)

 

def products(request,pk):
    projectObj = project.objects.get(id=pk)
   
    return render(request,'product.html',{'project':projectObj})

def create_project(request):
    form = projectForm()

    if request.method == 'POST':
        print(request.POST)
        form =projectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Hello')

       
    context = {'form':form}
    return render(request,'project_form.html',context)




#older codes

# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display work'
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by the community'
#     }
# ]
