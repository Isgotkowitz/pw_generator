from textdistance import damerau_levenshtein as func
import copy

def noSimiListFn(func, val):
	#dict = { "11111": "wall", "11112": "paper", "11113":"haskell", "11114": "well"}

	n = len(val)

	# initialize the nxn distance matrix 
	matrix = [[3 for x in range(n)] for y in range(n)] 
	
	# convert the dictionary to a list
	#val = list(dict.values())

	# compute each entry for the distance matrix
	for i in range(len(val)):
		for j in range(i + 1, len(val)):
			matrix[i][j] = func(val[i],val[j])

	# update the list according to the distance matrix	
	val2 = copy.copy(val)
	for i in range(len(val)):
		for j in range(i + 1, len(matrix[i])):
			if i != j and i > j and matrix[i][j] <= 2:
				if val[i] in val2:
					val2.remove(val[i])

	# return the list
	return val2
	
