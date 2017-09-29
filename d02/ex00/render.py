import sys
import os
import re

class FileReader:
	def __init__(self, filename):
		self.filename = filename
	def read_file(self):
		pass

class Render(FileReader):
	def __init__(self, filename, setting_filename):
		super().__init__(filename)
		self.settings = Settings(setting_filename)
	def process_line(self, line):
		html_line = line
		for cle in self.settings.params:
			html_line = html_line.replace("{" + cle + "}", self.settings.params[cle])
		return html_line

	def write_html(self, html_filename):
		f_html = open(html_filename, "w")
		try:
			with open(self.filename) as f:
				for line in f:
					html_line = self.process_line(line)
					f_html.write(html_line)
		except FileNotFoundError as e:
			print("File {0} Not found".format(e.filename))
			exit(1)
		f_html.close()

class Settings(FileReader):
	def __init__(self, filename):
		super().__init__(filename)
		self.read_file()
		
	def read_file(self):
		self.params = dict() # atribut
		try:
			with open(self.filename) as f:
				for line in f:
					data = line.split("=")
					self.params[data[0].strip(" ")] = data[1].strip("\" \n") # j'elimine les caraceteres inutiles
		except FileNotFoundError as e:
			print("File {0} not found".format(e.filename))
			exit(1)


def render(filename):
	file, file_extension = os.path.splitext(filename)
	if file_extension == ".template":
		t = Render(filename, "settings.py")
		t.write_html(file+".html")
	else:
		print("File {0} must have extension .template".format(filename))
if __name__ == '__main__' :
	if len(sys.argv) == 2:
	    render(sys.argv[1])