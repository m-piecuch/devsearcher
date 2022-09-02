from django.shortcuts import render

from django.http import HttpResponse




def projects(request):
    return HttpResponse(f'All projects on the {request.path} path')

def project(request, pk):
    return HttpResponse(f"Single project nr: {pk}")