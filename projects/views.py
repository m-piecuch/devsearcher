from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    projectsList = Project.objects.all()
    return render(request, 'projects/projects.html', {"projects": projectsList})


def project(request, pk):
    selected_project = Project.objects.get(id=pk)
    tags = selected_project.tags.all()
    return render(request, 'projects/single_project.html', {"projects": selected_project, "tags": tags})


def createProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm(instance=project)
    context = {
        'form': form,
        'isUpdating': True
               }
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {
        'project': project
    }
    return render(request, 'projects/delete_project.html', context)
    # project.delete()
    # return redirect('projects')