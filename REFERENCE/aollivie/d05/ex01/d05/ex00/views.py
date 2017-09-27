from django.shortcuts import render, HttpResponse
from .tool.ex00.Conn import Conn

# Create your views here.

def init(request):
    c = Conn()
    mess = c.execute_query(""" CREATE TABLE ex00_movies (
                    title varchar(64) UNIQUE NOT NULL,
                    episode_nb integer PRIMARY KEY,
                    opening_crawl text NULL,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date NOT NULL
                    ) """)
    return HttpResponse(mess)
