import numpy
import preprocess
import math
import sys

data= preprocess.train_preprocess()
charToIntDict=preprocess.test_preprocess()
charToInt = charToIntDict['cTable']

e = numpy.zeros((len(charToInt), 2, 2))
f = numpy.zeros((len(charToInt), 2, 2), dtype=numpy.int)
lamb = numpy.zeros((len(charToInt), 2, 2))
#init
for x in range(2):
	for y in range(2):
		for z in range(len(charToInt)):
			lamb[z][x][y] = 1.0
teta=10
alfa=0.001
alpha = [];
beta = [];

def get_alpha_beta():
	# l = len(charToInt);

	for sentence in data:
		sen_a = [];
		sen_b = [];
		l = len(sentence);
		sen_a.append((0.0, 1.0));
		sen_b.append((0.0, 1.0))
		for i in xrange(l-1):
			ci = charToInt.get(sentence[i][0]);
			na_0 = float(sen_a[i][0]*math.exp(lamb[ci][0][0])) + float(sen_a[i][1]*math.exp(lamb[ci][1][0]));
			na_1 = float(sen_a[i][0]*math.exp(lamb[ci][0][1])) + float(sen_a[i][1]*math.exp(lamb[ci][1][1]));
			sen_a.append((na_0, na_1));
			
			ci = charToInt.get(sentence[-i-1][0]);
			nb_0 = float(sen_b[0][0]*math.exp(lamb[ci][0][0])) + float(sen_b[0][1]*math.exp(lamb[ci][0][1]));
			nb_1 = float(sen_b[0][0]*math.exp(lamb[ci][1][0])) + float(sen_b[0][1]*math.exp(lamb[ci][1][1]));

			sen_b.insert(0, (nb_0, nb_1))

		alpha.append(sen_a);
		beta.append(sen_b);
	#print("alpha_beta done")
	####return alpha, beta



def e_f_train():
	for sent_ind in range(len(data)):
		sentence = data[sent_ind]
		for x in range(1, len(sentence)):
			(key, value) = sentence[x]
			char_ind = charToInt.get(key)
			tag_prev = sentence[x-1][1]
			tag = value
			z0 = float(beta[sent_ind][0][0]) + float(beta[sent_ind][0][1])
			if z0 == 0.0:
				z0 = 0.000000000000000000000000000001

			e[char_ind][0][0] += float(alpha[sent_ind][x-1][0] * beta[sent_ind][x][0] * math.exp(lamb[char_ind][0][0]))/ z0
			e[char_ind][0][1] += float(alpha[sent_ind][x-1][0] * beta[sent_ind][x][1] * math.exp(lamb[char_ind][0][1]))/ z0
			e[char_ind][1][0] += float(alpha[sent_ind][x-1][1] * beta[sent_ind][x][0] * math.exp(lamb[char_ind][1][0]))/ z0
			e[char_ind][1][1] += float(alpha[sent_ind][x-1][1] * beta[sent_ind][x][1] * math.exp(lamb[char_ind][1][1]))/ z0
			
			f[char_ind][tag_prev][tag] += 1
		
	#print("ef done")
	####return e,f

def SGD():
		#each lamda modified for one iteration
	for each_char in range(len(lamb)):
		for x in range(0,2):
			for y in range(0,2):
				delta_temp = float(f[each_char][x][y]) - float(e[each_char][x][y]) - float(lamb[each_char][x][y]/teta)
				lamb[each_char][x][y]= float(lamb[each_char][x][y]) + float(alfa*delta_temp)
	#print("SGD done")
	# return lamb

def viterbi(observes, probTable, charToInt):
	l = len(observes);
	states = numpy.zeros((l, 2));
	paths = numpy.zeros((l, 2), dtype = numpy.int);
	states[0][1] = 0;
	states[0][0] = -1e10;
	for i in xrange(1, l):
		k = charToInt[observes[i]];
		for j in xrange(0, 2):
			v1 = states[i-1][0] + probTable[k][0][j];
			v2 = states[i-1][1] + probTable[k][1][j];
			if( v1 > v2 ):
				states[i][j] = v1;
				paths[i][j] = 0;
			else:
				states[i][j] = v2;
				paths[i][j] = 1;
	ans = [];
	if(states[l-1][0] > states[l-1][1]):
		ans.insert(0, 0);
	else:
		ans.insert(0, 1);
	for i in reversed(xrange(1, l)):
		ans.insert(0, paths[i][ans[0]]);
	return ans;




#print data

for x in range(150):
	get_alpha_beta()
	e_f_train()
	SGD()
	# print alpha
	# print beta
	alpha = list();
	beta = list();

	e = numpy.zeros((len(charToInt), 2, 2))
	f = numpy.zeros((len(charToInt), 2, 2), dtype=numpy.int)


"""
print "f:"
for x in f:
	print x
print
"""
"""
print "lambda:"
for x in lamb:
	print x
print 
"""

test_data = charToIntDict['testData']

ans = list()
"""for sent in charToIntDict['testData']:
	if len(sent) > 0:
		ans.append(viterbi(sent, lamb, charToInt))
"""
##print charToIntDict['testData'][0]
for x in test_data:
	ans.append(viterbi(x, lamb, charToInt))


#print "Paths"
for sent_ind in range(len(ans)):
	sys.stdout.write(test_data[sent_ind][0].encode('UTF-8'))
	for i in range(1, len(test_data[sent_ind])):
		if ans[sent_ind][i] == 0:
			sys.stdout.write(test_data[sent_ind][i].encode('UTF-8'))
		else:
			sys.stdout.write(' '+test_data[sent_ind][i].encode('UTF-8'))
	print

