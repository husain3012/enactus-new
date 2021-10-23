from django.shortcuts import render
from django.http import request
from django.views.generic import TemplateView, DetailView, ListView
from . import models
import os

class Index(TemplateView):
    template_name = 'website/index.html'

class Featured(TemplateView):
    template_name = 'website/media.html'

class Gallery(TemplateView):
    template_name = 'website/gallery.html'

class Shrimati(TemplateView):
    template_name = 'website/shrimati.html'

def PrevProjectView(request):
    # project = models.Project.objects.all().filter(Current=False)
    # print(project)
    return render(request, "website/previous_projects.html", {})


def CurrProjectView(request):
    # project = models.Project.objects.all().filter(Current=True)
    # print(project)
    return render(request, 'website/current_projects.html', {})


def ImdaadView(request):
    # print(os.environ["MYVAR"])
    return render(request, 'website/imdaad.html', {})


def IrtiqaView(request):
    return render(request, 'website/irtiqa.html', {})

# class BlogListView(ListView):
#     model = models.Blog


def BlogListView(request):
    return render(request, 'website/blog.html', {})


def BambooView(request):
    return render(request, 'website/bamboo.html', {})

def MensurationView(request):
    return render(request, 'website/mensuration.html', {})

def MythView(request):
    return render(request, 'website/myths.html',{})

def ClimateView(request):
    return render(request,'website/climate.html',{})

def WaterView(request):
    return render(request,'website/water.html',{})
    
def SanotationView(request):
    return render(request, 'website/sanitation.html', {})


def WomenView(request):
    return render(request, 'website/women.html', {})


def BlogCategory(request):
    return render(request, 'website/garden-category.html', {})


class BlogDetailView(DetailView):
    model = models.Blog


class AboutUsView(TemplateView):
    template_name = 'website/Aboutus.html'
