from django.conf import settings
import requests
import json
import pickle
import random

class Data_mgmt:

	def get_strength(self):
		return len(self.dump()['Moviedex'])

	def load_default_settings(self):
		self.moviedex = []
		self.movielist = []
		self.position = settings.PLAYER_START
		self.nbr_balls = 3
		for name in settings.MOVIES:
			response = requests.get("http://www.omdbapi.com/?t=" + name + "&plot=short&r=json")
			self.movielist.append(json.loads(response.text))
		self.dic = {"position": self.position, "nbr_balls": self.nbr_balls, "Moviedex": self.moviedex, "Movies": self.movielist}
		self.picklize()

	def load(self, pos, balls, dex):
		self.movielist = self.dump()['Movies']
		self.moviedex = dex
		self.position = pos
		self.nbr_balls = balls
		self.dic = {"position": self.position, "nbr_balls": self.nbr_balls, "Moviedex": self.moviedex, "Movies": self.movielist}
		self.picklize()

	def dump(self):
		obj = self.unpicklize()
		return (obj)

	def get_random_movie(self):
		obj = self.dump()
		mv = obj['Movies']
		dex = obj['Moviedex']
		while len(dex) < len(mv):
			var = random.choice(mv)
			# start methode sale
			count = 0
			for i in dex:
				if dex[i]['Title'] == var['Title']:
					count += 1
			if count == 0:
				return var
			# end methode sale

	def get_movie(self, name):
		obj = self.dump()['Movies']
		for item in obj:
			if item['Title'] == name:
				return item

	def picklize(self):
		f = open("data_pickled", "wb")
		pickle.dump(self.dic, f)
		f.close()

	def unpicklize(self):
		f = open("data_pickled", "rb")
		obj = pickle.load(f)
		f.close()
		return obj
