import sys, json, requests, pickle, random, os
from django.conf import settings
from pygame import mixer

class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Soundmanager(object):
	__metaclass__ = Singleton

	def __init__(self):
		print('init')
		mixer.pre_init(48000, -16, 2, 2048)
		mixer.init()
	#	//file_path = '/path/to/sound.wav'
	#/	#file_wav = wave.open(file_path)
	#	frequency = file_wav.getframerate()

	@classmethod
	def play_song_main(cls):
		mixer.music.stop()
		mixer.music.load('Rush00/static/main_theme.mp3')
		mixer.music.play(-1)

	@classmethod
	def play_song_world(cls):
		mixer.music.stop()
		mixer.music.load('Rush00/static/goodbye_moon_men.mp3')
		mixer.music.play(-1)

	@classmethod
	def play_song_battle(cls):
		mixer.music.stop()
		mixer.music.load('Rush00/static/get_schwifty.mp3')
		mixer.music.play(-1)



class Datamanager(object):

	def __init__(self):
		print('Datamanager created')
		params = getattr(settings, "MOVIEMON", None)
		if not params:
			print('Missing setting MOVIEMON')
			movies = ['My Little Pony - Friendship is Magic']
		else:
			movies = params['MOVIES']
		self.lst = movies
		print('Movie list : ',self.lst)


	@classmethod
	def set_default(cls):
		params = getattr(settings, "MOVIEMON", None)
		if not params:
			print('Missing settings for MOVIEMON')
			cls.mapx = 50
			cls.mapy = 50
		else:
			pos = params['INITIAL_PLAYER_POS']
			cls.mapx = pos[0]
			cls.mapy = pos[1]
		cls.coord           = [1.352083, 103.819836]
		cls.movieballs      = 100
		cls.Moviemons       = {}
		cls.My_Moviemons    = []
		cls.MoviemonBattle  = ''
		cls.strength        = 0
		cls.index 			= 0

	@classmethod
	def set_value(cls,
					new_coordinates,
					new_movieballs,
					new_Moviemons,
					new_My_Moviemons,
					new_MoviemonBattle = [],
					new_strength = 0,
					new_mapx = 50,
					new_mapy = 50,
					new_index = 0):

		cls.coord           = new_coordinates
		cls.movieballs      = new_movieballs
		cls.Moviemons       = new_Moviemons
		cls.My_Moviemons    = new_My_Moviemons
		cls.MoviemonBattle  = new_MoviemonBattle
		cls.strength        = new_strength
		cls.mapx			= new_mapx
		cls.mapy            = new_mapy
		cls.index			= new_index

	@classmethod
	def move_coord(cls, x, y):
		coord[0] = x
		coord[1] = y

	@classmethod
	def modif_movieballs(cls, nb):
		cls.movieballs = nb

	@classmethod
	def add_moviemons(cls, name):
		cls.My_Moviemons.append(name)

	@classmethod
	def del_moviemons(cls, name):
		del cls.Moviemons[name]

	@classmethod
	def del_battlemovie(cls, moviemon_id):
		self.MoviemonBattle = ''


	def load(self, name):
		info = []
		print("Data Loading....... 1")
		print(name,os.path.isfile(name))
		if os.path.isfile(name):
			with (open(name, "rb")) as openfile:
				while True:
					try:
						print("Loading Game File -  :", name);
						info.append(pickle.load(openfile))
					except EOFError:
						break
			self.set_value(info[0][0],
						   info[0][1],
						   info[0][3],
						   info[0][2],
						   info[0][4],
						   info[0][5],
						   info[0][6],
						   info[0][7],
						   info[0][8])
			self.save('info.pickle')
			openfile.close()
			return info[0]
		return ("Free")
		#return redirect('/worldmap')

	def dump(self):
		info = []
		with (open("info.pickle", "rb")) as openfile:
			while True:
				try:
					info.append(pickle.load(openfile))
				except EOFError:
					break
		openfile.close()
		return info[0]

	def get_random_movie(self):
		my_mon = self.My_Moviemons
		mon = list(self.Moviemons.keys())
		return [x for x in mon if x not in my_mon]

	def load_default_settings(self):
		self.set_default()
		F = open("info.pickle", "wb")
		for item in self.lst:
			r = requests.get("http://www.omdbapi.com/?t=" + item + "&apikey=41f80ff7")
			if r.status_code != 200:
				raise Exception ("Error: " + str(r.status_code))
			Moviemon = json.loads(r.text)
			self.Moviemons[Moviemon['Title'].replace(" ", "_").replace(":", "-")] = Moviemon
		info = [
				self.coord,
				self.movieballs,
				self.My_Moviemons,
				self.Moviemons,
				self.MoviemonBattle,
				self.strength,
				self.mapx,
				self.mapy,
				self.index
		]

		pickle.dump(info, F)
		F.close()
		return info

	def get_strength(self):
		return len(self.My_Moviemons)

	def get_movie(self, name):
		return self.Moviemons[name]

	def get_all_movies(self):
		info = self.dump()
		return list(info[3].keys())

	def save(self, name):

		F = open(name, "wb")
		info = [
				self.coord,
				self.movieballs,
				self.My_Moviemons,
				self.Moviemons,
				self.MoviemonBattle,
				self.strength,
				self.mapx,
				self.mapy,
				self.index
			]

		pickle.dump(info, F)
		F.close()
