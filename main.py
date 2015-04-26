import numpy
import preprocess
import math

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
teta=4
alfa=1
alpha = [];
beta = [];

def get_alpha_beta():
    # l = len(charToInt);

    for sentence in data:
        sen_a = [];
        sen_b = [];
        l = len(sentence);
        sen_a.append((0, 1));
        sen_b.append((0.5, 0.5))
        for i in xrange(l):
            ci = charToInt.get(sentence[i][0]);
            na_0 = sen_a[i][0]*math.exp(lamb[ci][0][0]) + sen_a[i][1]*math.exp(lamb[ci][1][0]);
            na_1= sen_a[i][0]*math.exp(lamb[ci][0][1]) + sen_a[i][1]*math.exp(lamb[ci][1][1]);
            sen_a.append((na_0, na_1));
            
            ci = charToInt.get(sentence[-i-1][0]);
            nb_0 = sen_b[0][0]*math.exp(lamb[ci][0][0]) + sen_b[0][1]*math.exp(lamb[ci][0][1]);
            nb_1 = sen_b[0][0]*math.exp(lamb[ci][1][0]) + sen_b[0][1]*math.exp(lamb[ci][1][1]);
            sen_b.insert(0, (nb_0, nb_1));
        alpha.append(sen_a);
        beta.append(sen_b);
    print("alpha_beta done")
    ####return alpha, beta



def e_f_train():
	for sent_ind in range(len(data)):
	    sentence = data[sent_ind]
	for x in range(1, len(sentence)):
		(key, value) = sentence[x]
		char_ind = charToInt.get(key)
		tag_prev = sentence[x-1][1]
		tag = value
		f[char_ind][tag_prev][tag] += 1

		e[char_ind][0][0] += alpha[sent_ind][x-1][0] * beta[sent_ind][x][0] * math.exp(lamb[char_ind][0][0])
		e[char_ind][0][1] += alpha[sent_ind][x-1][0] * beta[sent_ind][x][1] * math.exp(lamb[char_ind][0][1])
		e[char_ind][1][0] += alpha[sent_ind][x-1][1] * beta[sent_ind][x][0] * math.exp(lamb[char_ind][1][0])
		e[char_ind][1][1] += alpha[sent_ind][x-1][1] * beta[sent_ind][x][1] * math.exp(lamb[char_ind][1][1])
	print("ef done")
    ####return e,f

def SGD():
		#each lamda modified for one iteration
	for each_char in range(len(lamb)):
		for x in range(0,2):
			for y in range(0,2):
				delta_temp=f[each_char][x][y]-e[each_char][x][y]-lamb[each_char][x][y]/teta
				lamb[each_char][x][y]=lamb[each_char][x][y]-alfa*delta_temp
	print("SGD done")
	# return lamb

def viterbi(observes, probTable, charToInt):
    l = len(observes);
    states = numpy.zeros((l, 2), dtype ='double');
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

get_alpha_beta()
e_f_train()
SGD()

ans = list()
"""for sent in charToIntDict['testData']:
	if len(sent) > 0:
		ans.append(viterbi(sent, lamb, charToInt))
"""
ans.append(viterbi(charToIntDict['testData'][0], lamb, charToInt))
ans.append(viterbi(charToIntDict['testData'][1], lamb, charToInt))
ans.append(viterbi(charToIntDict['testData'][2], lamb, charToInt))
ans.append(viterbi(charToIntDict['testData'][3], lamb, charToInt))
ans.append(viterbi(charToIntDict['testData'][4], lamb, charToInt))
ans.append(viterbi(charToIntDict['testData'][5], lamb, charToInt))
print "Paths"
print ans



