from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    return render(request, template) 


# Страница со списком мороженого
def group_posts(request):
    template = 'posts/group_list.html'
    return render(request, template)