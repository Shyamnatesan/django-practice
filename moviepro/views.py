from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies' : [
        {
            'id' : 5,
            'title' : 'Little Women',
            'year' : 2019
        },

        {
            'id' : 6,
            'title' : 'Lady Bird',
            'year' : 2017
        },

        {
            'id' : 7,
            'title' : 'Bullet Train',
            'year' : 2022
        }
    ]
}

def movies(request):
    return render(request, 'moviepro/moviepro.html', data)

def home(request):
    return HttpResponse("This is the Homepage!")