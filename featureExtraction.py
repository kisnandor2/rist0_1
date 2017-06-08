from createImage import *
from dummyData import *

def ftd(imageMatrix):
	#First time element is displaced
	n = len(imageMatrix[0])
	ret = [0]*n
	for i in range(0, n):
		moved = False
		for j in range(1, len(imageMatrix)):
			if imageMatrix[j-1][i] != imageMatrix[j][i]:
				ret[i] = j
				moved = True
			if moved:
				break
	ret = [x for (y,x) in sorted(zip(imageMatrix[0],ret))] #Sort ret by First row of matrix
	# print(sorted(imageMatrix[0]))
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
	for i in range(max(ftpList), 41):
		if imageMatrix[i] != imageMatrix[i+1]:
			print("ALMA")
	return max(ftpList)

def main():
	arg = 2
	data = loadData("data.csv", arg)
	imageMatrix = formatDataIntoMatrix(data)
	print(ftd(imageMatrix))
	print(ftp(imageMatrix))
	print(nit(ftp(imageMatrix)))

if __name__ == "__main__":
	main()