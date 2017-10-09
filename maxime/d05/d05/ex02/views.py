from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

def init(request):
	try:
		conn = psycopg2.connect(
				database='formationdjango',
				host='localhost',
				user='djangouser',
				password='secret'
			)

		curr = conn.cursor()

		curr.execute(""" CREATE TABLE IF NOT EXISTS ex02_movies (
			title varchar(64) UNIQUE NOT NULL,
			episode_nb integer PRIMARY KEY,
			opening_crawl text,
			director varchar(32) NOT NULL,
			producer varchar(128) NOT NULL,
			release_date date NOT NULL
			)
			""")

		conn.commit()
		conn.close()
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(e)

def populate(request):
	try:
		conn = psycopg2.connect(
				database='formationdjango',
				host='localhost',
				user='djangouser',
				password='secret'
			)

		curr = conn.cursor()
		db = 'ex02_movies'
		keys = 'episode_nb, title, director, producer, release_date'
		items = [
			(1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
			(2, 'Attack of the Clones', 'Georges Lucas', 'Rick McCallum', '2002-05-16'),
			(3, 'Revenge of the Sith', 'Georges Lucas', 'Rick McCallum', '2005-05-19'),
			(4, 'A New Hope', 'Georges Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
			(5, 'The Empire Strike Backs', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
			(6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, Georges Lucas, Rick McCallum', '1983-05-25'),
			(7, 'The Force Awakens', 'J.J. Abrams', 'Kathleen Kennedy, J.J. Abrams, Bryan Burk', '2015-02-11')
		]
		query = 'INSERT INTO {}({}) VALUES {}'
		p = []
		for item in items:
			query = query.format(db, keys, item)
			p.append(query)
			try:
				curr.execute(query, item)
				conn.commit()
			except Exception as e:
				return HttpResponse(e)
		conn.close()
	except Exception as e:
		return HttpResponse(e)
