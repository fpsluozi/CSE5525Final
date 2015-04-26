e = numpy.zeros((2,2,lenChatInt), dType=double)
f = numpy.zeros((2,2,lenChatInt), dType=double)
lamb = numpy.zeros((2,2,lenChatInt), dType=double)

for x in range(2):
	for y in range(2):
		for z in range(lenChatInt):
			lamb[x][y][z] = 1.0