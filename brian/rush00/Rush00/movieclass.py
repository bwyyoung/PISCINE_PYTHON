import sys, json, requests, pickle, random, os
from django.conf import settings
from distutils.version import LooseVersion, StrictVersion
import platform
if platform.release() <= "15.6.0":
	from pygame import mixer

class Singleton(type):
	_instances = {}
	def __call__(self, *args, **kwargs):
		if self not in self._instances:
			self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
		return self._instances[self]

class Soundmanager(object):
	__metaclass__ = Singleton

	def __init__(self):
		print('init')
		if platform.release() > "15.6.0":
			return
		mixer.pre_init(48000, -16, 2, 2048)
		mixer.init()
		Soundmanager.mute = True
		print(platform.platform())
		print(platform.system())
		print(platform.release())
		print(platform.version())
		print(sys.version_info)

	@classmethod
	def play_song_main(self):
		if platform.release() > "15.6.0":
			return
		if Soundmanager.mute:
			return
		mixer.music.stop()
		mixer.music.load('Rush00/static/main_theme.mp3')
		mixer.music.play(-1)

	@classmethod
	def play_song_world(self):
		if platform.release() > "15.6.0":
			return
		if Soundmanager.mute:
			return
		mixer.music.stop()
		mixer.music.load('Rush00/static/goodbye_moon_men.mp3')
		mixer.music.play(-1)

	@classmethod
	def play_song_battle(self):
		if platform.release() > "15.6.0":
			return
		if Soundmanager.mute:
			return
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


	@classmethod
	def set_default(self):
		params = getattr(settings, "MOVIEMON", None)
		if not params:
			print('Missing settings for MOVIEMON')
			self.mapx = 50
			self.mapy = 50
		else:
			pos = params['INITIAL_PLAYER_POS']
			self.mapx = pos[0]
			self.mapy = pos[1]
		self.coord           = [1.352083, 103.819836]
		self.movieballs      = 100
		self.Moviemons       = {}
		self.My_Moviemons    = []
		self.MoviemonBattle  = ''
		self.strength        = 0
		self.index 			= 0

	@classmethod
	def set_value(self,
					new_coordinates,
					new_movieballs,
					new_Moviemons,
					new_My_Moviemons,
					new_MoviemonBattle = [],
					new_strength = 0,
					new_mapx = 50,
					new_mapy = 50,
					new_index = 0):

		self.coord           = new_coordinates
		self.movieballs      = new_movieballs
		self.Moviemons       = new_Moviemons
		self.My_Moviemons    = new_My_Moviemons
		self.MoviemonBattle  = new_MoviemonBattle
		self.strength        = new_strength
		self.mapx			= new_mapx
		self.mapy            = new_mapy
		self.index			= new_index

	@classmethod
	def move_coord(self, x, y):
		self.coord[0] = x
		self.coord[1] = y

	@classmethod
	def modif_movieballs(self, nb):
		self.movieballs = nb

	@classmethod
	def add_moviemons(self, name):
		self.My_Moviemons.append(name)

	@classmethod
	def del_moviemons(self, name):
		del self.Moviemons[name]

	def load(self, name):
		info = []
		print("Data Loading....... 1")
		print(name, os.path.isfile(name))
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
		print('LOAD DEFAULT SETTINGS')
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
		print(self.Moviemons)

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
