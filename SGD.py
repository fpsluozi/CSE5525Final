def SGD(E,F,Lam):


	#delta
	# delta for each lamda
	#each lamda modified for one iteration
	for each_char in lam:
		for x in range(0,2):
			for y in range(0,2):
				delta_temp=F[each_char][x][y]-E[each_char][x][y]-lam[each_char][x][y]/teta
				lam[each_char][x][y]=lam[each_char][x][y]-alfa*delta_



	#test convergence



	return lam
