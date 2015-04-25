def train_preprocess():
	lines = []
	#f1 = open("test.utf8", 'r')
	f1 = open('as_training.utf8', 'r')
	trainingText = f1.readlines()
	#trainingText = trainingText.encode('UTF-8')
	segments = []
	trainData = []
	for line in trainingText:
		lines.append(line.decode('utf-8'))
		#print line.decode('utf-8')
		segment = []
		start = True
		trainLine = []
		for character in line.decode('utf-8'):
			if(character==' ' or character=='\n'):
				start = True
				continue
			if(start is True):
				segment.append(1)
			if(start is False):
				segment.append(0)
			start = False
			trainLine.append(character)
		segments.append(segment)
		trainData.append(trainLine)

	return trainData, segments
def test_preprocess():
	lines = []
	f2 = open('as_test.utf8', 'r')
	testText = f2.readlines()
	testData = []

	for line in testText:
		lines.append(line.decode('utf-8'))
		#print line.decode('utf-8')
		testLine = []
		for character in line.decode('utf-8'):
			
			if(character=='\n'):
				start = True
				continue
			testLine.append(character)
		testData.append(testLine)
	return testData