e = numpy.zeros((lenCharInt, 2, 2), dType=double)
f = numpy.zeros((lenCharInt, 2, 2), dType=double)
lamb = numpy.zeros((lenCharInt, 2, 2), dType=double)

for x in range(2):
	for y in range(2):
		for z in range(lenCharInt):
			lamb[z][x][y] = 1.0