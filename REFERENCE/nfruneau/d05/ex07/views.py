from django.shortcuts import render, HttpResponse
import psycopg2
from ex07.models import Movies

# Create your views here.

def index(request):
	return HttpResponse("ex07")

def populate(request):
	try:
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
			m = Movies(
				episode_nb=item[0],
				title=item[1],
				director=item[2],
				producer=item[3],
				release_date=item[4]
				)
			m.save()
			mess.append(item[1] + " => OK<br>")
		return HttpResponse(mess)
	except Exception as e:
		return HttpResponse(e)

def display(request):
	try:
		r = Movies.objects.all()
		l = []
		for row in r:
			lr = (row.episode_nb, row.title, row.opening_crawl,row.director, row.producer, row.release_date, row.created, row.updated)
			l.append(lr)
		if l == []:
			raise Exception ()
		return render(request, "ex02/display.html", {'data' : l})
	except Exception as e:
		return HttpResponse("No data available")

def update(request):
	try:
		if (request.method == "POST"):
			form = request.POST
			if len(form['crawling_text']) > 0:
				m = Movies.objects.get(episode_nb=int(form['title']))
				m.opening_crawl = form['crawling_text']
				m.save()

		response = Movies.objects.all()
		l = []
		for row in response:
			dat = (row.title, row.episode_nb)
			l.append(dat)
		if l == []:
			raise Exception ()
		return render(request, "ex06/update_form.html", {'data' : l})
	except Exception as e:
		return HttpResponse("No data available")
