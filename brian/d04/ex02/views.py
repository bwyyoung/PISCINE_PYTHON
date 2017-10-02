from django.shortcuts import render, HttpResponse
from ex02.forms import MyForm
import datetime
import os.path
from django.conf import settings


def hist_filename():
	hist = getattr(settings, "HISTORY_FILE", None)
	if not hist:
		hist = 'default.log'
	return hist


def read_history():
	hist_list = []
	if os.path.isfile(hist_filename()):
		with open(hist_filename()) as f:
			hist_list = f.readlines()
	return hist_list


def add_history(msg):
	f = open(hist_filename(),'a')
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
