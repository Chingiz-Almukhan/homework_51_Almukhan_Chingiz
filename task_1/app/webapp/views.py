

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.db import data, links
from webapp.state import change_state, check_data


def home_view(request: WSGIRequest):
    return render(request, 'main_page.html')


def stats(request):
    if request.POST:
        data.update({'name': request.POST.get('name')})
        data.update({'image': links[0]})

    return render(request, 'cat_stats.html', context={
        'image': data.get('image'),
        'name': data.get('name'),
        'age': data.get('age'),
        'happiness': data.get('happiness'),
        'satiety': data.get('satiety')
    })


def change(request):
    change_state(request.POST)
    check_data(data)
    return redirect('http://127.0.0.1:8000/cat_stats/')
