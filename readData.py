import csv
import numpy as np

from linecache import getline

def loadData(fileName = "data.csv", lineIndex = None):
	# Reads the data from the csv
	print("LoadingData...")
	if lineIndex is not None:
		if lineIndex < 1:
			raise Exception("Invalid argument lineIndex")
		return getline(fileName, lineIndex+1)
	with open(fileName ,'r') as dest_f:
			data_iter = csv.reader(dest_f, 
														 delimiter = ',', 
														 quotechar = '"')
			data = [data for data in data_iter]
	data_array = np.asarray(data)
	print("DataLoading DONE")
	return data_array

def splitDataIntoLabelsAndImages(data):
	# Formats the data into a dictionary, like: {label1: [imagesForLabel1], label2: etc.}
	print("SplittingDataForLaterUse")
	for i in range(1, len(data)): # Convert strings to float
		data[i] = np.asfarray(data[i])
	ret = {}
	for i in range(1, len(data)):
		label = int(float(data[i][0]))
		row = data[i].tolist()
		row.pop(0) # Remove the label part from image data
		if not label in ret:
			ret[label] = []
		ret[label].append(row)
	print("Data splitting DONE")
	return ret

def printLabelNumberOfSamples(data):
	totalNumberOfLabels = 0
	totalNumberOfSamples = 0
	for label in data:
		totalNumberOfLabels += 1
		totalNumberOfSamples += len(data[label])
	# print("Total number of Labels: {0}".format(totalNumberOfLabels))
	# print("Total number of Samples: {0}".format(totalNumberOfSamples))
	print(totalNumberOfLabels)
	print(totalNumberOfSamples)
	for label in data:
		print("{0}, {1}".format(int(label), len(data[label])))
		# print("Label, numberOfSamples: {0}, {1}".format(int(label), len(data[label])))

def main():
	data = loadData()
	data = splitDataIntoLabelsAndImages(data)
	printLabelNumberOfSamples(data)

if __name__ == "__main__":
	main()
