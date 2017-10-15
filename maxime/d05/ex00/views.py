from django.shortcuts import render
import psycopg2

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
        release_date date NOT NULL
    ); '''.format(name))

def init(request):
    exception = ''
    try:
        conn = None
        #try:
        conn = __connect_to_db()
        __create_table(conn, 'ex00_movies')
        conn.commit()
    except Exception as e:
        exception = e
    return render(request, 'ex00/base.html', {'body_data': "OK" if not exception else exception})

# Create your views here.
