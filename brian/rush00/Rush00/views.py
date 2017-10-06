from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from .forms import MyForm
import random
from .movieclass import Datamanager
from .movieclass import Soundmanager

def New(request):
	print (request)
	if request.GET.get('a') == 'a':
		db = Datamanager()
		db.load_default_settings()
		db.save("save.pickle")
		Soundmanager().play_song_world()
		return redirect('/worldmap')
	if request.GET.get('a') == 'b':
		return redirect('/options/load_game')
	Soundmanager().play_song_main()
	return render(request, "Rush00/new.html")


def Options(request):
	if request.GET.get('a') == 'start':
		return redirect('/worldmap')
	if request.GET.get('a') == 'a':
		return redirect('/options/save_game')
	if request.GET.get('a') == 'b':
		return redirect('/')
	return render(request, "Rush00/options.html")



def calcul(strengthMovie, strengthPlayer):
	C = 50 - (float(strengthMovie) * 10) + (strengthPlayer * 5)
	if C < 1:
		C = 1
	if C > 90:
		C = 90
	return C

def capture(C):
	if random.randint(0,100) < C:
		return (True)
	return (False)

def OptionsSave(request):
	my_database = Datamanager()
	data_player = []
	data_monster = []
	slots = ["slotA.pickle", "slotB.pickle", "slotC.pickle"]
	save_slot_indices = ["slotA", "slotB", "slotC"]
	i = 0
	for slot in slots:
		my_database.load(slot)
		data_player.append([ slot[0:5], len(my_database.My_Moviemons)])
		data_monster.append([slot[0:5], len(my_database.Moviemons)])
		i+=1

	db = Datamanager()
	db.load("save.pickle")
	index = db.index;

	db.index = index;
	if request.GET.get('a') == 'up':
		db.index = (db.index - 1) % 3
	if request.GET.get('a') == 'down':
		db.index = (db.index + 1) % 3

	if request.GET.get('process') == '1':
		db.save(slots[db.index])

	print(db.index)

	db.save("save.pickle")
	if request.GET.get('a') == 'start':
		return redirect('/options/save_game')
	if request.GET.get('a') == 'a':
		return redirect('/options/save_game?process=1')
	if request.GET.get('a') == 'b':
		return redirect('/options')
	return render(request, "Rush00/optionsSave.html", {"slots":slots, "data_monster":data_monster,"data_player":data_player, "name":save_slot_indices[db.index]})


def OptionsLoad(request):
	my_database = Datamanager()
	data_player = []
	data_monster = []
	slots = ["slotA.pickle", "slotB.pickle", "slotC.pickle"]
	save_slot_indices = ["slotA", "slotB", "slotC"]
	i = 0
	for slot in slots:
		my_database.load(slot)
		data_player.append([ slot[0:5], len(my_database.My_Moviemons)])
		data_monster.append([slot[0:5], len(my_database.Moviemons)])
		i += 1

	db = Datamanager()
	db.load("save.pickle")
	index = db.index
	db.index = index
	if request.GET.get('a') == 'up':
		db.index = (db.index - 1) % 3
	if request.GET.get('a') == 'down':
		db.index = (db.index +1) % 3

	if request.GET.get('process') == '1':
		db.load(slots[db.index])
		print('LOADED DATA')
		Soundmanager().play_song_world()
		return redirect('/worldmap')

	db.save("save.pickle")
	if request.GET.get('a') == 'start':
		return redirect('/options/load_game')
	if request.GET.get('a') == 'a':
		return redirect('/options/load_game?process=1')
	if request.GET.get('a') == 'b':
		return redirect('/')
	return render(request, "Rush00/optionsLoad.html", {"slots":slots, "data_monster":data_monster,"data_player":data_player, "name":save_slot_indices[db.index]})


def Moviedex(request):
	db = Datamanager()
	db.load("save.pickle")
	newdico = {}

	if request.GET.get('a') == 'select':
		return redirect('/worldmap')

	if (len(db.My_Moviemons)):
		for elem in db.My_Moviemons:
			newdico[elem] = db.Moviemons[elem]

		db.My_Moviemons.sort()

		print(db.index)
		if (len(db.My_Moviemons)):
			if request.GET.get('a') == 'right':
				db.index = (db.index + 1) %len(db.My_Moviemons)
			if request.GET.get('a') == 'left':
				db.index = (db.index + -1) %len(db.My_Moviemons)
			db.save("save.pickle")

		if request.GET.get('a') == 'a':
			return redirect('/moviedex/'+db.My_Moviemons[db.index])


		db.My_Moviemons.sort()
		return render(request, "Rush00/moviedex.html", {"dico": newdico, "cursor": db.My_Moviemons[db.index]})
	else:
		return render(request, "Rush00/moviedex.html")


def MoviedexDetail(request, moviemon_id):
	db = Datamanager()
	db.load("save.pickle")

	if request.GET.get('a') == 'b':
		return redirect('/moviedex')
	return render(request, "Rush00/moviedexdetail.html", {"detail": db.Moviemons[moviemon_id]})


def Battle(request, moviemon_id):
	battle_commentary = ""
	print (request, moviemon_id)
	db = Datamanager()
	db.load("save.pickle")

	if moviemon_id not in db.My_Moviemons:
		if len(db.MoviemonBattle) > 0:
			print(db.MoviemonBattle)
			moviemon_id = db.MoviemonBattle
		elif moviemon_id in db.Moviemons:
			db.MoviemonBattle = moviemon_id
		else:
			return redirect('/')
		if request.GET.get('a') == 'a':
			if db.movieballs > 0:
				db.movieballs -= 1
				if (capture(calcul(db.Moviemons[moviemon_id]['imdbRating'], db.strength))):
					db.My_Moviemons.append(moviemon_id)
					battle_commentary = moviemon_id +  " Captured !"
					db.MoviemonBattle = ""
					db.strength += 1
			else:
				battle_commentary = "You ran out of Balls! Press B to quit battle..."

	if request.GET.get('a') == 'b':
		db.MoviemonBattle = []
		db.save("save.pickle")
		Soundmanager().play_song_world()
		return redirect('/worldmap')

	print("Print db.moviemon: ",moviemon_id , " : \n",db.Moviemons[moviemon_id])
	print("NB balls:",db.movieballs)

	# if moviemon_id in db.Moviemons:
	# 	db.add_moviemons(moviemon_id)
	db.save("save.pickle")
	return render(request, "Rush00/battle.html", {
		"Dictionary_Movie":db.Moviemons[moviemon_id],
		"movieballs": db.movieballs,
		"battle_commentary": battle_commentary,
		"strength": db.strength,
		"Luck": calcul(db.Moviemons[moviemon_id]['imdbRating'], db.strength)
	})

params = getattr(settings, "MOVIEMON", None)
if not params:
	print('Missing setting MOVIEMON')
	MAPMIN = 0 # par defaut
	MAPMAX = 100 # par defaut
else:
	pos = params['GRID_SIZE']
	MAPMIN = pos[0]
	MAPMAX = pos[1]
print('MAPMIN = ', MAPMIN)
print('MAPMAX = ', MAPMAX)


def Worldmap(request):
	db = Datamanager()
	db.load("save.pickle")
	choix = ['left', 'right','up', 'down']
	# if request.GET in choix


	if request.GET.get('a') == "select":
		return redirect('/moviedex')
	if request.GET.get('a') == "start":
		return redirect('/options')

	miv = 0
	rand = 0
	etat = "balade"
	if len(db.MoviemonBattle) == 0:
		if request.GET.get('a') in choix:
			if request.GET.get('a') == 'left' and db.mapx > MAPMIN:
				db.mapx-=1
				db.coord[1]-=0.0010
				miv = 1
			if request.GET.get('a') == 'right' and db.mapx < MAPMAX:
				db.mapx+=1
				db.coord[1]+=0.0010
				miv = 1
			if request.GET.get('a') == 'up' and db.mapy > MAPMIN:
				db.mapy-=1
				db.coord[0]+=0.0010
				miv = 1
			if request.GET.get('a') == 'down' and db.mapy < MAPMAX:
				db.mapy+=1
				db.coord[0]-=0.0010
				miv = 1

			if (miv):
				rand = random.randint(1,100)
				if rand > 60 and len(db.get_random_movie()) > 0: #A VERIF
					print("Moviemon trouve", random.choice(db.get_random_movie()))
					etat = "attack"
					db.MoviemonBattle = random.choice(db.get_random_movie())
				elif rand > 40:
					db.modif_movieballs(db.movieballs+1)
					print("Movieball trouve")
					etat = "ball"


	if len(db.MoviemonBattle) > 0:
		etat = "attack"
		print(db.MoviemonBattle)
		if request.GET.get('a') == 'a':
			Soundmanager().play_song_battle()
			return redirect('/battle/'+db.MoviemonBattle)
		elif request.GET.get('a') == 'b':
			db.MoviemonBattle = ""
			etat = "balade"
	db.save("save.pickle")

	return render(request, "Rush00/game.html", {
													"latitude":db.coord[0],
													"longitude":db.coord[1],
													"movieball": db.movieballs,
													"movietitle":db.MoviemonBattle,
													"etat":etat,
													"mapx":db.mapx,
													"mapy":db.mapy
	})


def Form(request):
	if (request.method == 'POST'):
		form = MyForm(request.POST)
		if form.is_valid():
			return HttpResponse("Form Valid %s -----------   %s" %(form.cleaned_data['name'], form.cleaned_data['email']))
		else:
			return HttpResponse("NON")
	else:
		form = MyForm()
	return render(request, "Rush00/form.html", {'form' : form})
