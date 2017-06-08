from createImage import *
import operator
# from dummyData import *

def ftd(imageMatrix):
	#First time element is displaced
	n = len(imageMatrix[0])
	m = len(imageMatrix)
	ret = [0]*n
	for i in range(0, n):
		moved = False
		for j in range(1, m):
			if imageMatrix[j-1][i] != imageMatrix[j][i]:
				ret[i] = j
				moved = True
			if moved:
				break
	# print(imageMatrix[0])
	# print(ret)
	ret = [x for (y,x) in sorted(zip(imageMatrix[0],ret))] #Sort ret by First row of matrix
	# print(sorted(imageMatrix[0]))
	if Order.checkDecreasing(imageMatrix[m-1]):
		ret.reverse();
	return ret

def ftp(imageMatrix):
	#First time element is in it's final place
	n = len(imageMatrix[0])
	m = len(imageMatrix)-1
	ret = [-1]*n
	for i in range(0, n):
		final = False
		for j in range(m-1, -1, -1):
			if imageMatrix[m][i] != imageMatrix[j][i]:
				ret[i] = j+1
				final = True
			if final:
				break
	# print(imageMatrix[m])
	return ret;

def nit(ftpList):
	#Number of steps to reach final state
	return max(ftpList)

def rpa(ftdList, ftpList):
	return sum(list(map(operator.sub, ftpList, ftdList)))

def main():
	arg = 5
	data = loadData("data.csv", arg)
	imageMatrix = formatDataIntoMatrix(data)
	_ftd = ftd(imageMatrix)
	_ftp = ftp(imageMatrix)
	_nit = nit(_ftp)
	_rpa = rpa(_ftd, _ftp)
	print("{0}\n{1}\n{2}\n{3}".format(_ftd, _ftp, _nit, _rpa))

if __name__ == "__main__":
	main()