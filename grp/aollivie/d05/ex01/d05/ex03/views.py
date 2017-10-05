from django.shortcuts import render, HttpResponse
from .tool.Conn import Conn
from datetime import date
from .tool import elements as e
from .tool.elem import Text
from .Movies import Movies
# Create your views here.

def init(request):
    c = Conn()
    mess = c.execute_query(""" CREATE TABLE ex02_movies (
                    title varchar(64) UNIQUE,
                    episode_nb integer PRIMARY KEY,
                    opening_crawl text,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date
                    ) """)
    c.close()
    return HttpResponse(mess)

def populate(request):
    mess = ''
    good = ''
    try:
        m = Movies(
            episode_nb = 1 , title = 'The Phantom Menace' ,
            director = 'George Lucas',
            producer = 'Rick McCallum' , release_date = '1999-05-19'
        )
        mess = 'The Phantom Menace'
        m.save()
        good += ' OK '
        m = Movies(
            episode_nb = 2 , title = 'Attack of the Clones' ,
            director = 'George Lucas' , producer = 'Rick McCallum' ,
            release_date = '2002-05-16'
        )
        mess = 'Attack of the Clones'
        m.save()
        good += ' OK '
        m = Movies(episode_nb = 3 , title = 'Revenge of the Sith' ,
        director = 'George Lucas' , producer ='Rick McCallum' ,
        release_date = '2005-05-19'
        )
        mess = 'Revenge of the Sith'
        m.save()
        good += ' OK '
        m = Movies(episode_nb = 4 , title = 'A New Hope' ,
        director = 'George Lucas' , producer = 'Gary Kurtz, Rick McCallum' ,
        release_date = '1977-05-25'
        )
        mess = 'A New Hope'
        m.save()
        good += ' OK '
        m = Movies(episode_nb = 5 , title = 'The Empire Strikes Back' ,
        director = 'Irvin Kershner' ,
        producer = 'Gary Kutz, Rick McCallum' , release_date = '1980-05-17'
        )
        mess = 'The Empire Strikes Back'
        m.save()
        good += ' OK '
        m = Movies(episode_nb = 6 , title = 'Return of the Jedi' ,
        director = 'Richard Marquand' , producer= 'Howard G. Kazanjian, George Lucas, Rick McCallum' , release_date = '1983-05-25'
        )
        mess = 'Return of the Jedi'
        m.save()
        good += ' OK '
        m = Movies(episode_nb = 7 , title = 'The Force Awakens' ,
        director = 'J. J. Abrams' , producer = 'Kathleen Kennedy, J. J. Abrams, Bryan Burk' ,
        release_date = '2015-12-11'
        )
        mess = 'The Force Awakens'
        mess += ' - '
        m.save()
        good += ' OK '
    except Exception as e:
        return HttpResponse(str(mess + str(e)))
    return HttpResponse(good)


def display(request):
    m = Movies()
    result = Movies.objects.all()
    # return HttpResponse('ok')
    if result == None:
        return HttpResponse("No data available")
    tr = []

    # print(result)
    for r in result:
        tr.append(e.Tr(e.Td([e.Text(str(r.episode_nb) ),
         e.Text(str(r.title) ),
         e.Text(str(r.director) ),
         e.Text(str(r.producer) ),
         e.Text(str(r.release_date) ),
         e.Text(str(r.opening_crawl) )
         ]
        )))
    table = e.Table(tr)

    return HttpResponse(table)
