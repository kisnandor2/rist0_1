from matplotlib import pyplot as plt

from readData import *
from checkData import Order

from sys import argv, exc_info

def printToImage(data):
	plt.imshow(data, cmap='gray', interpolation='nearest', vmin=0, vmax=255)
	plt.savefig('image.png')

def formatDataIntoMatrix(data):
	try:
		data = np.fromstring(data, sep=",").tolist()
		data.pop(0)
	except Exception as e:
		data = np.asfarray(data) 
	return np.array(data).reshape(42, 10)*255

def main():
	data = None
	try:
		arg = int(argv[1])
		data = loadData("data.csv", arg)
		data = formatDataIntoMatrix(data)
		printToImage(data)
		print('Image rendering done');
	except Exception as e:
		print(e)
		print('Usage: {0} indexOfImageRow'.format(argv[0]))
		return
	lastRow = data[len(data)-1];
	print("Order: {0}".format(Order.checkOrder(lastRow)))
	


if __name__ == "__main__":
	main()
	
