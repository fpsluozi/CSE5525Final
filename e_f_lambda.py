# chartoInt = {(字, 下标)}
# lenCharInt = len(chartoInt)

e = numpy.zeros((lenCharInt, 2, 2), dType=double)
f = numpy.zeros((lenCharInt, 2, 2), dType=int)
lamb = numpy.zeros((lenCharInt, 2, 2), dType=double)

for x in range(2):
	for y in range(2):
		for z in range(lenCharInt):
			lamb[z][x][y] = 1.0

for sent_ind in range(len(data)):
	sentence = data[sent_ind]
	for x in range(1, len(sentence)):
		(key, value) = sentence[x]
		char_ind = chartoInt.get(key)
		tag_prev = sentence[x-1][1]
		tag = value
		f[char_ind][tag_prev][tag] += 1

		e[char_ind][0][0] += alpha[sent_ind][x-1][0] * beta[sent_ind][x][0] * exp(lamb[char_ind][0][0])
		e[char_ind][0][1] += alpha[sent_ind][x-1][0] * beta[sent_ind][x][1] * exp(lamb[char_ind][0][1])
		e[char_ind][1][0] += alpha[sent_ind][x-1][1] * beta[sent_ind][x][0] * exp(lamb[char_ind][1][0])
		e[char_ind][1][1] += alpha[sent_ind][x-1][1] * beta[sent_ind][x][1] * exp(lamb[char_ind][1][1])
		


