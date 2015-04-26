cTable = {}
cNo = 0
def train_preprocess():
	lines = []
	#f1 = open("test.utf8", 'r')
	f1 = open('as_training.utf8', 'r')
	trainingText = f1.readlines()
	#trainingText = trainingText.encode('UTF-8')
	trainData = []
	global cTable
	global cNo
	for line in trainingText:
		lines.append(line.decode('utf-8'))
		#print line.decode('utf-8')
		start = True
		trainLine = []

		for character in line.decode('utf-8'):
			if(character==' ' or character=='\n'):
				start = True
				continue
			if(start is True):
				trainTuple = (character, 1)
			if(start is False):
				trainTuple = (character, 0)
			start = False
			trainLine.append(trainTuple)
			if(character not in cTable):
				cTable.update({character: cNo})
				cNo = cNo + 1
				
		trainData.append(trainLine)

	return trainData
def test_preprocess():
	lines = []
	f2 = open('as_test.utf8', 'r')
	testText = f2.readlines()
	testData = []
	global cTable
	global cNo
	for line in testText:
		lines.append(line.decode('utf-8'))
		#print line.decode('utf-8')
		testLine = []
		for character in line.decode('utf-8'):
			
			if(character=='\n'):
				start = True
				continue
			testLine.append(character)
			if(character not in cTable):
				cTable.update({character: cNo})
				cNo = cNo + 1
		testData.append(testLine)
	return testData, cTable