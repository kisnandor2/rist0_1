from featureExtraction import *
from dummyData import data

def getNitAndRpaForAllImages(data):
	ret = {}
	for label in data:
		ret[label] = {
			"nit": [],
			"rpa": [],
			"ftd": [],
			"ftp": []
		}
		for image in data[label]:
			imageMatrix = formatDataIntoMatrix(image)
			_ftd = ftd(imageMatrix)
			_ftp = ftp(imageMatrix)
			_nit = nit(_ftp)
			_rpa = rpa(_ftd, _ftp)
			ret[label]["nit"].append(_nit)
			ret[label]["rpa"].append(_rpa)
			ret[label]["ftd"].append(_ftd)
			ret[label]["ftp"].append(_ftp)
	return ret

def printHistograms(data = None):
	if data is None:
		data = loadData("data.csv")
	else:
		print("---------\nWorking with dummy data\n---------\n")
	data = splitDataIntoLabelsAndImages(data)
	ret = getNitAndRpaForAllImages(data)
	for label in ret:
		plt.hist(ret[label]["nit"], 100, normed=1, facecolor='green', alpha=0.75)
		plt.savefig('histNitLabel{0}.png'.format(label))
		plt.close()
		plt.hist(ret[label]["rpa"], 100, normed=1, facecolor='green', alpha=0.75)
		plt.savefig('histRpaLabel{0}.png'.format(label))
		plt.close()

def addAvg(avg, item):
	if isinstance(item, list):
		return list(map(operator.add, avg, item))
	return avg+item
def divAvg(avg, count):
	if isinstance(avg, list):
		return list(map(operator.truediv, avg, [count]*len(avg)))
	return avg/count
def addStdDev(stdDev, avg, item):
	if isinstance(item, list):
		return list(map(operator.add,list(map(operator.pow, list(map(operator.sub, avg, item)), [2]*len(item))), stdDev))
	return stdDev + pow(item-avg, 2)

def divStdDev(stdDev, count):
	return divAvg(stdDev, count)
def initAvg(feature):
	if feature == "ftd" or feature == "ftp":
		return [0]*10
	return 0
def initStdDev(feature):
	return initAvg(feature)

def getAvgAndStdDev(data = None, feature = None):
	if data is None:
		data = loadData("data.csv")
	else:
		print("---------\nWorking with dummy data\n---------\n")
	data = splitDataIntoLabelsAndImages(data)
	nit_rpa = getNitAndRpaForAllImages(data)
	ret = {}
	for label in nit_rpa:
		sortLabel = label//2
		avg = initAvg(feature)
		for item in nit_rpa[label][feature]:
			avg = addAvg(avg, item)
		avg = divAvg(avg, len(nit_rpa[label][feature]))
		stdDev = initStdDev(feature)
		for item in nit_rpa[label][feature]:
			stdDev = addStdDev(stdDev, avg, item)
		stdDev = divStdDev(stdDev, len(nit_rpa[label][feature]))
		ret[sortLabel] = {
				"avg": avg,
				"stdDev": stdDev 
		}
	return ret

def main(data = None):
	# print(getAvgAndStdDev(data, "ftp"))	
	printHistograms()

if __name__ == "__main__":
	main(data)