from django.shortcuts import render, HttpResponse
import psycopg2

# Create your views here.

def index(request):
	return HttpResponse("ex02")

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
			episode_nb  integer PRIMARY KEY,
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

		l = [
			(1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
			(2, 'Attack of the Clones', 'Georges Lucas', 'Rick McCallum', '2002-05-16'),
			(3, 'Revenge of the Sith', 'Georges Lucas', 'Rick McCallum', '2005-05-19'),
			(4, 'A New Hope', 'Georges Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
			(5, 'The Empire Strike Backs', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
			(6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, Georges Lucas, Rick McCallum', '1983-05-25'),
			(7, 'The Force Awakens', 'J.J. Abrams', 'Kathleen Kennedy, J.J. Abrams, Bryan Burk', '2015-02-11')
		]

		mess = []
		for item in l:
			try:
				curr.execute(" INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES (%s,%s,%s,%s,%s)",
				(item[0], item[1], item[2], item[3], item[4]))
				conn.commit()
				mess.append(item[1] + " => OK<br>")
			except Exception as e:
				mess.append(item[1] + ": " + e.args[0] + "<br>")
				conn.commit()

		conn.close()
		return HttpResponse(mess)
	except Exception as e:
		return HttpResponse(e)

def display(request):
	try:
		conn = psycopg2.connect(
				database='formationdjango',
				host='localhost',
				user='djangouser',
				password='secret'
			)

		curr = conn.cursor()

		curr.execute(""" SELECT * FROM ex02_movies """)
		response = curr.fetchall()
		l = []
		for row in response:
			l.append(row)
		conn.close()
		if l == []:
			raise Exception ()
		return render(request, "ex02/display.html", {'data' : l})
	except Exception as e:
		return HttpResponse("No data available")
