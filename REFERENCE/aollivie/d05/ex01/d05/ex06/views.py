from django.shortcuts import render, HttpResponse
from .tool.Conn import Conn
from datetime import date
from .tool import elements as e
from .tool.elem import Text
import datetime
# Create your views here.

def init(request):
    c = Conn()
    mess = c.execute_query(""" CREATE TABLE ex06_movies (
                    title varchar(64) UNIQUE,
                    episode_nb integer PRIMARY KEY,
                    opening_crawl text,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date,
                    created timestamp default now(),
                    updated timestamp default now()

                    ) """)
    c.execute_query('CREATE OR REPLACE FUNCTION update_changetimestamp_column() \
    RETURNS TRIGGER AS $$ \
    BEGIN \
    NEW.updated = now();\
    NEW.created = OLD.created;\
    RETURN NEW;\
    END;\
    $$ language "plpgsql";\
    CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE\
    ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE\
    update_changetimestamp_column();')
    c.close()
    return HttpResponse(mess)

def populate(request):
    c = Conn()

    mess = c.insert('ex06_movies',{'created':str(datetime.datetime.now()), 'updated': str(datetime.datetime.now()),
        'episode_nb' : 1 , 'title' : 'The Phantom Menace' ,
        'director' : 'George Lucas',
        'producer' : 'Rick McCallum' , 'release_date' : '1999-05-19'
    }, 'The Phantom Menace ')
    c.close()
    c = Conn()
    mess += ' - '
    mess += c.insert('ex06_movies',{'created':str(datetime.datetime.now()), 'updated': str(datetime.datetime.now()),
        'episode_nb' : 2 , 'title' : 'Attack of the Clones' ,
        'director' : 'George Lucas' , 'producer' : 'Rick McCallum' ,
        'release_date' : '2002-05-16'
    }, 'Attack of the Clones ')
    c.close()
    c = Conn()
    mess += ' - '
    mess += c.insert('ex06_movies',{'created':str(datetime.datetime.now()), 'updated': str(datetime.datetime.now()),'episode_nb' : 3 , 'title' : 'Revenge of the Sith' ,
    'director' : 'George Lucas' , 'producer' :'Rick McCallum' ,
    'release_date' : '2005-05-19'
    }, 'Revenge of the Sith ')
    c.close()
    c = Conn()
    mess += ' - '
    mess += c.insert('ex06_movies',{'created':str(datetime.datetime.now()), 'updated': str(datetime.datetime.now()),'episode_nb' : 4 , 'title' : 'A New Hope' ,
    'director' : 'George Lucas' , 'producer' : 'Gary Kurtz, Rick McCallum' ,
    'release_date' : '1977-05-25'
    }, 'A New Hope ')
    c.close()
    c = Conn()
    mess += ' - '
    mess += c.insert('ex06_movies',{'created':str(datetime.datetime.now()), 'updated': str(datetime.datetime.now()),'episode_nb' : 5 , 'title' : 'The Empire Strikes Back' ,
    'director' : 'Irvin Kershner' ,
    'producer' : 'Gary Kutz, Rick McCallum' , 'release_date' : '1980-05-17'
    }, 'The Empire Strikes Back ')
    c.close()
    c = Conn()
    mess += ' - '
    mess += c.insert('ex06_movies',{'created':str(datetime.datetime.now()), 'updated': str(datetime.datetime.now()),'episode_nb' : 6 , 'title' : 'Return of the Jedi' ,
    'director' : 'Richard Marquand' , 'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum' , 'release_date' : '1983-05-25'
    }, 'Return of the Jedi ')
    c.close()
    c = Conn()
    mess += ' - '
    mess += c.insert('ex06_movies',{'created':str(datetime.datetime.now()), 'updated': str(datetime.datetime.now()),'episode_nb' : 7 , 'title' : 'The Force Awakens' ,
    'director' : 'J. J. Abrams' , 'producer' : 'Kathleen Kennedy, J. J. Abrams, Bryan Burk' ,
    'release_date' : '2015-12-11'
    }, 'The Force Awakens ')
    c.close()
    return HttpResponse(mess)


def display(request):
    c = Conn()
    param = {'values': '*', 'table': 'ex06_movies'}
    result = c.select(param)
    c.close()
    if result == None or len(result) == 0:
        return HttpResponse("No data available")
    tr = []

    for r in result:

        td =[]
        for v in r:
            print(v)
            td.append(e.Td(Text(str(v))))
        tr.append(e.Tr(td))
    table = e.Table(tr)

    return HttpResponse(table)

def update(request):
    c = Conn()
    if request.method == 'POST':
        if 'opening_crawl' in  request.POST:
            print(str(request.POST['title']))
            print(str(request.POST['opening_crawl']))
            c.execute_query('UPDATE  ex06_movies SET opening_crawl = ' + "'" +str(request.POST['opening_crawl']) + "'" + '  WHERE title=' + "'" + str(request.POST['title']) + "'")

    param = {'values': 'title', 'table': 'ex06_movies'}
    result = c.select(param)
    c.close()
    if result == None:
        return HttpResponse("No data available")

    content = []
    # content.append(e.Text('{% csrf_token %}'))
    for r in result:
        content.append(
        e.Option(attr={'value':str(r[0])})
        )
        content.append(
        e.Text(str(r[0]))
        )
    if len(content) == 0:
        return HttpResponse("No data available")
    content.append(e.Input(attr={'type':'text', 'name':'opening_crawl'}))
    content.append(e.Input(attr={'type':'submit', 'name':'submit', 'value':'Submit'}))
    form = e.Select(content, attr={'name':'title'})
    return render(request, 'ex04/base.html', {'form': form})
    return HttpResponse(form)
