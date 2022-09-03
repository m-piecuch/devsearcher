from multiprocessing import context
from django.shortcuts import render

projects = [
    {
        'id': '1',
        'title': 'Maverick',
        'description': 'The best USA movie about the planes.'
    },
    {
        'id': '1',
        'title': 'Maverick',
        'description': 'The best USA movie about the planes.'
    
    },
    {
        'id': '1',
        'title': 'Maverick',
        'description': 'The best USA movie about the planes.'
    },
    {
        'id': '1',
        'title': 'Maverick',
        'description': 'The best USA movie about the planes.' 
    }
]



def projects(request):
    page = 'page dage'
    context = {
        'projects': projects,
        'message': page,
        'username': 'Janusz',
        'isAuthenticated': True
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    return render(request, 'projects/single_project.html')