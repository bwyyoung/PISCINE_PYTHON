from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movies

def __get_data():
    return [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19'
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16'
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19'
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25'
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kutz, Rick McCallum',
            'release_date': '1980-05-17'
        },
        {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25'
        },
        {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J. J. Abrams',
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
            'release_date': '2015-12-11'
        },
    ]

def populate(request):
    data = __get_data()
    response = []
    for movie in data:
        try:
            Movies.objects.create(**movie)
            response.append("OK")
        except Exception as e:
            response.append(str(e))
    return render(request, 'ex05/as_it.html', {'body_data': response})

def display(request):
    try:
        queryset = Movies.objects.all()
    except:
        queryset = []
    return render(request, "ex05/display.html", {'queryset': queryset})

def remove(request):

    if 'id' in request.POST:
        try:
            get_object_or_404(Movies, episode_nb=int(request.POST['id'])).delete()
        except:
            pass
    try:
        queryset = Movies.objects.all()
    except:
        queryset = []
    return render(request, "ex05/remove.html", {'queryset': queryset})
