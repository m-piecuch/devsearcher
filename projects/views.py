from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


def projects(request):
    projectsList = Project.objects.all()
    return render(request, 'projects/projects.html', {"projects": projectsList})


def project(request, pk):
    selected_project = Project.objects.get(id=pk)
    tags = selected_project.tags.all()
    return render(request, 'projects/single_project.html', {"projects": selected_project, "tags": tags} )


def createProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)