from createImage import *
import operator
# from dummyData import *

def ftd(imageMatrix):
	#First time element is displaced
	n = len(imageMatrix[0])
	m = len(imageMatrix)
	ret = [0]*n
	for i in range(0, n):
		for j in range(1, m):
			if imageMatrix[j-1][i] != imageMatrix[j][i]:
				ret[i] = j
				break
	ret = [x for (y,x) in sorted(zip(imageMatrix[0],ret))] #Sort ret by First row of imageMatrix
	if Order.checkDecreasing(imageMatrix[m-1]): 
		ret.reverse(); #It has to be in increasing order
	return ret

def ftp(imageMatrix):
	#First time element is in it's final place
	n = len(imageMatrix[0])
	m = len(imageMatrix)-1
	ret = [-1]*n
	for i in range(0, n):
		for j in range(m-1, -1, -1):
			if imageMatrix[m][i] != imageMatrix[j][i]:
				ret[i] = j+1
				break
	if Order.checkDecreasing(imageMatrix[m]): # If it's in decreasing order make it increasing
			ret.reverse()
	return ret;

def nit(ftpList):
	#Number of steps to reach final state
	return max(ftpList)

def rpa(ftdList, ftpList):
	return sum(list(map(operator.sub, ftpList, ftdList)))

def main():
	arg = None
	try:
		arg = int(argv[1])
		data = loadData("data.csv", arg)
	except Exception as e:
		print(e)
		print('Usage: {0} indexOfImageRow'.format(argv[0]))
		return
	imageMatrix = formatDataIntoMatrix(data)
	print("ftd, ftp, nit, rpa:")
	_ftd = ftd(imageMatrix)
	_ftp = ftp(imageMatrix)
	_nit = nit(_ftp)
	_rpa = rpa(_ftd, _ftp)
	print("{0}\n{1}\n{2}\n{3}".format(_ftd, _ftp, _nit, _rpa))

if __name__ == "__main__":
	main()
