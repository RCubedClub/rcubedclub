from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import project, information, teams, list_of_keys
from .forms import projectForm, teamsForm, edit, editForm


# Create your views here.

def all_project(request):
    queryset = project.objects.all()
    info = information.objects.all().order_by('-id')[:3]
    context = {
        "object_list": queryset,
        "title": "List of All Projects",
        "info": info,
    }
    return render(request, "index.html", context)


def project_detail(request, id=None):
    form = edit(request.POST or None, request.FILES or None)
    instance = get_object_or_404(project, id=id)
    info = information.objects.all().order_by('-id')[:3]

    if form.is_valid():
        if instance.key == form.cleaned_data['key']:
            return HttpResponseRedirect("http://rcubedclub.herokuapp.com/edit/"+str(instance.id))

    context = {
        "instance": instance,
        "info": info,
        "form": form,
    }
    return render(request, "detail.html", context)


def add_project(request):
    form = projectForm(request.POST or None, request.FILES or None)
    info = information.objects.all().order_by('-id')[:3]

    if form.is_valid():
        pro = form.cleaned_data['project_title']
        check_key = form.cleaned_data['key']

        if len(list_of_keys.objects.filter(key__iexact=check_key))==1 and len(project.objects.filter(project_title__iexact=pro))==0:
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect("http://rcubedclub.herokuapp.com/projects/")

        else:
            info = information.objects.all().order_by('-id')[:3]
            context = {
              "form": form,
              "Error": "Please fill out the correct ceredentials.",
              "info": info,
            }
            return render(request, "create.html", context)

    context = {
        "form": form,
        "info": info,
    }
    return render(request, "create.html", context)

def homepage(request):
    info = information.objects.all().order_by('-id')[:3]
    projects = project.objects.all()[:3]
    slideshow1 = information.objects.all()[0]
    slideshow2 = information.objects.all()[1]
    slideshow3 = information.objects.all()[2]
    context = {
       "info": info,
        "object": projects,
        "slideshow1": slideshow1,
        "slideshow2": slideshow2,
        "slideshow3": slideshow3,
    }
    return render(request, "index1.html", context)

def teams_list(request):
    form = teamsForm(request.POST or None, request.FILES or None)
    info = information.objects.all().order_by('-id')[:3]
    list_of_teams = teams.objects.all()

    if form.is_valid():
        check_key = form.cleaned_data['Key']
        #print(len(teams.objects.filter(Key__contains=check_key)))

        if len(list_of_keys.objects.filter(key__iexact=check_key))==1 and len(teams.objects.filter(Key__iexact=check_key))==0:
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect("http://rcubedclub.herokuapp.com/members/")

        else:
            form = teamsForm(request.POST or None, request.FILES or None)
            info = information.objects.all().order_by('-id')[:3]
            list_of_teams = teams.objects.all()

            context = {
              "form": form,
              "Error": "Please fill out the correct ceredentials.",
              "info": info,
              "members": list_of_teams,
            }
            return render(request, "teams.html", context)

    context = {
       "info": info,
       "form": form,
       "members": list_of_teams,
    }
    return render(request, "teams.html", context)

def editproject(request, id=None):
    instance = get_object_or_404(project, id=id)
    form = editForm(request.POST or None, request.FILES or None, instance=instance)
    form1 = edit(request.POST or None)
    info = information.objects.all().order_by('-id')[:3]

    if form.is_valid() and form1.is_valid():
        if instance.key == form1.cleaned_data['key']:
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect("http://rcubedclub.herokuapp.com/details/"+str(instance.id))
        else:
            context = {
              "info": info,
              "form": form,
              "form1": form1,
              "Error": "Please fill out the correct ceredentials.",
            }
            return render(request, "edit.html", context)

    context = {
        "info": info,
        "form": form,
        "form1": form1,

    }
    return render(request, "edit.html", context)