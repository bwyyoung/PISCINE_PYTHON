from django.shortcuts import render, HttpResponse
from .tool.ex01.Conn import Conn

# Create your views here.

def init(request):
    c = Conn()
    mess = c.execute_query(""" CREATE TABLE ex00_movies (
                    title varchar(64) UNIQUE,
                    episode_nb integer PRIMARY KEY,
                    opening_crawl text,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date
                    ) """)
    return HttpResponse(mess)
