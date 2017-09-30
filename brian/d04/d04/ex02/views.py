from django.shortcuts import render, HttpResponse
from ex02.forms import MyForm
import datetime
import os.path
from django.conf import settings

# Create your views here.

hist_filename = getattr(settings, "HISTORY_FILE", None)
if not hist_filename:
	hist_filename = 'default.log'


def read_history():
	histo = []
	if os.path.isfile(hist_filename) : # on ne lit que si le fichier existe
		with open(hist_filename) as f:
			histo = f.readlines()
	return histo


def add_history(msg):
	f = open(hist_filename,'a')
	f.write(msg+'\n')
	f.close()


def ex02(request):
	msgs = read_history()
	if request.method == 'POST':
		form = MyForm (request.POST)
		if form.is_valid():
			date = datetime.datetime.now()
			msg = form.cleaned_data['message']
			msg += ' ' + str(date)
			add_history(msg)
			msgs.append(msg)
	else:
		form = MyForm()
	return render(request, 'ex02/form.html', {'form': form, 'msgs': msgs})
