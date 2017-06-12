from readData import *
from random import seed, uniform

def getTrainingAndValidationSetUniformly(formattedData):
	#TODO: Not sure if this is useful :/
	print("Splitting data to Training/Validation UNIFORMLY")
	seed(0.15) # To be able to reproduce the sample
	training = {}
	validation = {}
	for key in formattedData:
		if key not in training:
			training[key] = []
			validation[key] = []
		for i in range(0, len(formattedData[key])):
			if uniform(0,1) < 0.8:
				training[key].append(formattedData[key][i])
			else:
				validation[key].append(formattedData[key][i])
	print("Splitting done")
	return training, validation

def getTrainingAndValidationSetExactly(formattedData):
	print("Splitting data to Training/Validation EXACLTLY")
	training = {}
	validation = {}
	for key in formattedData:
		if key not in training:
			training[key] = []
			validation[key] = []
		lenT = len(formattedData[key]) * 80 // 100
		training[key] = formattedData[key][:lenT]
		validation[key] = formattedData[key][lenT:]
	print("Splitting done")
	return training, validation 

def formatDataForClassifier(data):
	print("Formatting data for classifier")
	ret = []
	labels = []
	for label in data:
		ret += data[label]
		labels += [label]*len(data[label])
	print("Formatting DONE")
	return ret, labels

# data = loadData()
# splittedData = splitDataIntoLabelsAndImages(data)
# training, validation = getTrainingAndValidationSetUniformly(splittedData)
# training, validation = getTrainingAndValidationSetExactly(splittedData)
