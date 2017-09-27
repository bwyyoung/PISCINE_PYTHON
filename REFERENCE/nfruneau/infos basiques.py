# protip pour debug : `from IPython import embed; embed()`
# ou ipdb

# ex00: var + type associé
# """
# print('var is of type', type(var), 'and value', var)
# """
# ex01: open file, read file, print
# ex02: liste de couple a passer en dictionnaire (clé/valeur), print
# ex03: recoupement de dictionnaires
# ex04: idem + argv
# ex05: recherche dans dictionnaire (matching)
# ex06: sort dictionnary
# ex07: data to html


# labels
def your_function(arg1="defaut1",arg2="defaut2",arg3="defaut3"):
	"""
		infos provided by help()
	"""
	print(arg1)
	print(arg2)
	print(arg3)

if __name__ == '__main__':
	your_function(arg2="val2", arg1="val1")
	# help(your_function)
	#function lambda:
	modifier = lambda x : x / 10
	print(modifier(2))


# tools:

# get len
# len(var)

# print substring, operator ":"
# print(tab[2:4])

# copy string into another:
# method str.replace
# access to all methods help(type) or dir(type) in console

# method format
# use {} in string puis method .format (possibilité de labels)
# ou %s puis % pour remplacer


# containers

# list:
# var = [1, 'b', 3.4]
# var = list()
# var.append(value)
# print(var)
# access to elem: var[num]

# tuple:
# non mutable
# var = (1, 'b', 2.3)
# var = tuple()
# print(var)
# access to elem: var[num]

# range: (utile pour itération)
# non mutable
# (value sera toujours de type numerique)
# var = range(value)
# var = range(value, value)
# convertir en list pour impression
# var = list(range(value, value, value))
# print(var)

# hash_table (dictionnary):
# ordre non ordonné
# var = {'key':value} (any type of value)
# var = dict()
# var['key'] = value
# print(var)


# operators:
# /		<- division reelle
# //	<- division sous forme d'int
# **	<- power operator
# +		<- concatenation de string

# conditions:
# if condition : elif condition : else: (no parenthesis)
# /!\ true != false != none
# ==	<- comparateur de valeur
# is	<- comparateur de type
# in	<- find in sequence

# boucles:

# i = 0
# while i < condition :
# 		...
# 		i += 1

# for var in range(value):
# 		print(var)

# for key, value in my_dict.items():
#		print(key, ':', value)

# comprehension: (example to get a list of even squared numbers)
# l = [i ** 2 for i in range(10) if i % 2 == 0]

# I/O file system:
# f = open("filename", 'w')
# f.write("lolo")
# f.close

# with open("filename", 'r') as f:
# for line in f :
#	print(line)

# argv:
# import sys
# print(sys.argv)
