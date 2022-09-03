from multiprocessing import context
from django.shortcuts import render

projectsList = [
    {
        'id': '1',
        'title': 'Maverick',
        'description': 'The best movie about planes.'
    },
    {
        'id': '2',
        'title': 'Terminator',
        'description': 'The best movie about robots.'
    
    },
    {
        'id': '3',
        'title': 'Green Mile',
        'description': 'The best movie about jails.'
    },
    {
        'id': '4',
        'title': 'Titanic',
        'description': 'The best movie about ships.' 
    }
]



def projects(request):
    page = 'page dage'
    context = {
        'projects': projectsList,
        'message': page,
        'username': 'Janusz',
        'isAuthenticated': True
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    index = int(pk) - 1
    item_to_show = projectsList[index]
    context = {
        "projects": item_to_show,
    }
    return render(request, 'projects/single_project.html', context)