import sys
import os
import re


class Filereader:
	def __init__(self, filename):
		self.filename = filename

	def read_file(self):
		pass


class Cvrender(Filereader):
	def __init__(self, filename, setting_filename):
		super().__init__(filename)
		self.settings = Cvsettings(setting_filename)

	def write_html(self, html_filename):
		try:
			f_html = open(html_filename, "w")
			with open(self.filename) as f:
				for line in f:
					html_line = self.process_line(line)
					f_html.write(html_line)

			f_html.close()
		except FileNotFoundError as e:
			print("File {0} Not found".format(e.filename))
			exit(1)

	def process_line(self, line):
		html_line = line
		for cle in self.settings.params:
			html_line = html_line.replace("{" + cle + "}", self.settings.params[cle])
		return html_line




class Cvsettings(Filereader):
	def __init__(self, filename):
		super().__init__(filename)
		self.read_file()

	def read_file(self):
		self.params = dict()
		try:
			with open(self.filename) as f:
				for line in f:
					data = line.split("=")
					self.params[data[0].strip(" ")] = data[1].strip("\" \n") # j'elimine les caraceteres inutiles
		except FileNotFoundError as e:
			print("File {0} not found".format(e.filename))
			exit(1)


def rendercv(filename):
	file, file_extension = os.path.splitext(filename)
	if file_extension == ".template":
		t = Cvrender(filename, "settings.py")
		t.write_html(file+".html")
	else:
		print("File {0} must have extension .template".format(filename))


if __name__ == '__main__' :
	if len(sys.argv) == 2:
		try:
				rendercv(sys.argv[1])
		except Exception as e:
			print("Unknown Error: {0}".format(sys.exc_info()[0]))
			exit(1)
