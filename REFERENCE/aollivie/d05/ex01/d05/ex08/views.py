from django.shortcuts import render, HttpResponse
from .tool.Conn import Conn
from datetime import date
from .tool import elements as e
from .tool.elem import Text
import datetime
from django.conf import settings
import os
# Create your views here.

def init(request):
    c = Conn()
    mess = c.execute_query(""" CREATE TABLE ex08_planets (
                    id serial PRIMARY KEY,
                    name varchar(64) UNIQUE NOT NULL,
                    climate varchar NULL,
                    diameter integer NULL,
                    orbital_period integer NULL,
                    population bigint NULL,
                    rotation_period integer NULL,
                    surface_water real NULL,
                    terrain varchar(128) NULL
                    ) """)
    mess += ' - '
    c.close()
    c = Conn()
    mess += c.execute_query(""" CREATE TABLE ex08_people (
                    id serial PRIMARY KEY,
                    name varchar(64) UNIQUE NOT NULL,
                    birth_year varchar(32) NULL,
                    gender varchar(32) NULL,
                    eye_color varchar(32) NULL,
                    hair_color varchar(32) NULL,
                    height integer NULL,
                    mass real NULL,
                    homeworld  varchar(64) NULL REFERENCES ex08_planets (name)
                    ) """)
    c.close()
    return HttpResponse(mess)

def populate(request):
    c = Conn()

    mess = ''
    col = ('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain')
    mess += str(c.copy_from(str(os.path.join(str(settings.BASE_DIR), str('ex08/planets.csv'))), str('ex08_planets'), str('\t'), col, str('NULL')))
    c.close()
    c = Conn()
    mess += ' - '
    col = ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld')
    mess += str(c.copy_from(os.path.join(settings.BASE_DIR, 'ex08/people.csv'), 'ex08_people', '\t', col, str('NULL')))
    c.close()
    return HttpResponse(mess)


def display(request):
    c = Conn()
    query = """SELECT p.name, p.homeworld, pp.climate  FROM ex08_people as p, ex08_planets as pp WHERE pp.name = p.homeworld AND pp.climate LIKE '%windy%' ORDER BY p.name"""
    c.curr.execute(query)
    result = c.curr.fetchall()
    c.conn.commit()
    print(result)
    # result = c.select(param)
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
