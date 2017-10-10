from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies
# https://docs.djangoproject.com/fr/1.11/topics/db/queries/
# https://www.webforefront.com/django/multiplemodelrecords.html
# https://stackoverflow.com/questions/12784835/django-no-such-table

def index(request):
	return HttpResponse('hello')


def populate(request):
	items = [
		{'episode_nb': 1, 'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '1999-05-19'},
		{'episode_nb': 2, 'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2002-05-16'},
		{'episode_nb': 3, 'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2005-05-19'},
		{'episode_nb': 4, 'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1977-05-25'},
		{'episode_nb': 5, 'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kutz, Rick McCallum', 'release_date': '1980-05-17'},
		{'episode_nb': 6, 'title': 'Return of the Jedi', 'director': 'Richard Marquand','producer':  'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date': '1983-05-25'},
		{'episode_nb': 7, 'title': 'The Force Awakens', 'director': 'J.J. Abrams', 'producer': 'Kathleen Kennedy, J.J. Abrams, Bryan Burk', 'release_date': '2015-12-11'}
	]
	trace = []
	for item in items:
		try:
			elem = Movies(**item)
			elem.save()
			trace.append('<p>{} => <span style="color:green">OK</span></p>'.format(elem))
		except Exception as e:
			trace.append('<p>{} => <span style="color:red">ERROR: {}</span></p>'.format(elem, e))
	return HttpResponse(trace)


def display(request):
	trace = []
	try:
		items = Movies.objects.all().values()
		for item in items:
			trace.append(item)
		return render(request, 'ex03/display.html', {'data' : trace})
	except:
		return HttpResponse('No data available')
