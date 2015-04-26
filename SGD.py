def SGD(E,F,L):


	#delta
	# delta for each lamda
	#all lamda modifed for one iteration
	for each_char in lam:
		for x in range(0,2):
			for y in range(0,2):
				delta_temp=F[each_char][x][y]-E[each_char][x][y]-lam[each_char][x][y]/teta
				lam[each_char][x][y]=lam[each_char][x][y]-alfa*delta_temp



	#test convergence



	return lam
