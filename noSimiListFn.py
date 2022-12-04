from textdistance import damerau_levenshtein as func
import copy

def noSimiListFn(func, dict):
	dict = { "11111": "wall", "11112": "paper", "11113":"haskell", "11114": "well"}

	n = len(dict)

	# initialize the nxn distance matrix 
	matrix = [[0 for x in range(n)] for y in range(n)] 
	
	# convert the dictionary to a list
	val = list(dict.values())

	# compute each entry for the distance matrix
	for i in range(len(val)):
		for j in range(len(val)):
			matrix[i][j] = func(val[i],val[j])

	# update the list according to the distance matrix	
	val2 = copy.copy(val)
	for i in range(len(val)):
		for j in range(len(matrix[i])):
			if i != j and i > j and matrix[i][j] <= 2:
				if val[i] in val2:
					val2.remove(val[i])

	# return the list
	return val2
	
