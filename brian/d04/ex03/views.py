from django.shortcuts import render


def ex03(request):
	return render(request, 'ex03/color.html')
