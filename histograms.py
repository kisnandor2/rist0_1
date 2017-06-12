from featureExtraction import *
from math import sqrt

def getNitAndRpaForAllImages(data):
	print("Getting NIT and RPA for all")
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
			m = len(imageMatrix)-1
			# Set ftd and ftp order for all to increasing
			if Order.checkDecreasing(imageMatrix[m]):
				_ftd.reverse()
				_ftp.reverse()
			ret[label]["ftd"].append(_ftd)
			ret[label]["ftp"].append(_ftp)
	print("NIT/RPA DONE")
	return ret

def printHistograms(data = None):
	print("Printing histograms to local directory")
	if data is None:
		data = loadData("data.csv")
		data = splitDataIntoLabelsAndImages(data)
	ret = getNitAndRpaForAllImages(data)
	for label in ret:
		plt.hist(ret[label]["nit"], 100, normed=1, facecolor='green', alpha=0.75)
		plt.savefig('histNitLabel{0}.png'.format(label))
		plt.close()
		plt.hist(ret[label]["rpa"], 100, normed=1, facecolor='green', alpha=0.75)
		plt.savefig('histRpaLabel{0}.png'.format(label))
		plt.close()
	print("Histograms DONE")

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
	avg = divAvg(stdDev, count)
	if isinstance(avg, list):
		for i in range(0, len(avg)):
			avg[i] = sqrt(avg[i])
		return avg
	return sqrt(avg)

def initAvg(feature):
	if feature == "ftd" or feature == "ftp":
		return [0]*10
	return 0
def initStdDev(feature):
	return initAvg(feature)

def getAvgAndStdDev(data = None, feature = None, nit_rpa = None):
	if data is None and nit_rpa is None:
		data = loadData("data.csv")
		data = splitDataIntoLabelsAndImages(data)
	if nit_rpa is None:
		nit_rpa = getNitAndRpaForAllImages(data)
	ret = {}
	for label in nit_rpa:
		sortLabel = label
		if label%2 == 1:
			sortLabel = label-1
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

def printIt(data):
	for key in data:
		print("Label: {0}".format(key))
		print(data[key]['avg'])
		print(data[key]['stdDev'])
	print('\n')

def printAvgs(data = None):
	data = loadData("data.csv")
	data = splitDataIntoLabelsAndImages(data)
	nit_rpa = getNitAndRpaForAllImages(data)
	_nit = getAvgAndStdDev(data, "nit", nit_rpa = nit_rpa)
	print("nit avg")
	printIt(_nit)
	_rpa = getAvgAndStdDev(data, "rpa", nit_rpa = nit_rpa)
	print("rpa avg")
	printIt(_rpa)
	_ftd = getAvgAndStdDev(data, "ftd", nit_rpa = nit_rpa)
	print("ftd avg")
	printIt(_ftd)
	_ftp = getAvgAndStdDev(data, "ftp", nit_rpa = nit_rpa)
	print("ftp avg")
	printIt(_ftp)
	return data # Just to save the reading time

if __name__ == "__main__":
	# TODO: don't use data like this
	data = printAvgs()
	printHistograms(data)