
def invert_dict(d):
	dates = dict()
	for name in d: ##parse the existing dictionary using names
		if dates.get(d[name]): #if I already have a date which is repeated
			dates[d[name]].append(name) #I append the name to the date which has another name attached.
		else:
			dates[d[name]] = [name] #create a new entry with a date key, and a name key.
	return dates

def sort_list():
	d = {
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939',
	}
	my_list = sorted(invert_dict(d).items())  #sort by date

	for tup in my_list:
		names = sorted(tup[1]) #sort by name in the date entry.
		for n in names: #print the names under the matching date.
			print(n)

if __name__ == '__main__' :
	sort_list()