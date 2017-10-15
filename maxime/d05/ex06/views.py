from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import psycopg2

TABLE = 'ex06_movies'

def __connect_to_db():
    return psycopg2.connect(
        database='formationdjango',
        host='localhost',
        user='djangouser',
        password='secret'
    )

def __create_table(conn, name):
    curr = conn.cursor()
    curr.execute(''' CREATE TABLE IF NOT EXISTS {} (
        title varchar(64) UNIQUE NOT NULL,
        episode_nb serial PRIMARY KEY,
        opening_crawl text,
        director varchar(32) NOT NULL,
        producer varchar(128) NOT NULL,
        release_date date NOT NULL,
        created timestamp,
        updated timestamp
    ); '''.format(name))
    curr.execute(''' CREATE OR REPLACE FUNCTION update_changetimestamp_column()
RETURNS TRIGGER AS $$
BEGIN
NEW.updated = now();
NEW.created = OLD.created;
RETURN NEW;
END;
$$ language 'plpgsql';
CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
update_changetimestamp_column() ;''')

def init(request):
    exception = ''
    try:
        conn = None
        conn = __connect_to_db()
        __create_table(conn, TABLE)
        conn.commit()
    except Exception as e:
        exception = e
    return render(request, 'ex06/base.html', {'body_data': "OK" if not exception else exception})

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

def __insert(conn, name, **kwargs):
    curr = conn.cursor()
    curr.execute('''
    INSERT INTO {} (title, director, producer, release_date, created, updated)
        VALUES ('{title}', '{director}', '{producer}', '{release_date}', now(), now())
    '''.format(name, **kwargs))

def populate(request):
    data = __get_data()
    response = []
    try:
        for movie in data:
            try:
                conn = __connect_to_db()
                __insert(conn, TABLE, **movie)
                conn.commit()
                response.append("OK")
            except Exception as e:
                response.append(movie['title'] + ' : ' + str(e))
    except Exception as e:
        response.append(str(e))
    return render(request, 'ex06/as_it.html', {'body_data': response})

def display(request):
    try:
        conn = __connect_to_db()
        curr = conn.cursor()
        curr.execute('SELECT * FROM {} ;'.format(TABLE))
        res = curr.fetchall()
        queryset = [{
            'title': a[0],
            'episode_nb': a[1],
            'opening_crawl': a[2],
            'director': a[3],
            'producer': a[4],
            'release_date': a[5],
            'created': a[6],
            'updated': a[7],
        } for a in res]
    except:
        queryset = []
    return render(request, "ex06/display.html", {'queryset': queryset})

def update(request):

    if 'id' in request.POST and 'text' in request.POST:
        try:
            i = int(request.POST['id'])
            conn = __connect_to_db()
            curr = conn.cursor()
            curr.execute(''' UPDATE {} SET opening_crawl = %s WHERE episode_nb = %s ; '''.format(TABLE), (request.POST['text'], i))
            conn.commit()
        except:
            pass
    try:
        conn = __connect_to_db()
        curr = conn.cursor()
        curr.execute('SELECT * FROM {} ;'.format(TABLE))
        res = curr.fetchall()
        queryset = [{
            'title': a[0],
            'episode_nb': a[1],
            'opening_crawl': a[2],
            'director': a[3],
            'producer': a[4],
            'release_date': a[5],
        } for a in res]
    except:
        queryset = []
    return render(request, "ex06/update.html", {'queryset': queryset})
