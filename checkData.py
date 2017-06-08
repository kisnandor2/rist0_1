from enum import Enum

class Order(Enum):
	INCREASING = 1
	DECREASING = 2
	UNORDERED = -1

	@staticmethod
	def checkIncreasing(list):
		for i in range(0, len(list)-1):
			if list[i] > list[i+1]:
				return False
		return True

	@staticmethod
	def checkDecreasing(list):
		for i in range(0, len(list)-1):
			if list[i] < list[i+1]:
				return False
		return True

	@staticmethod
	def checkOrder(list):
		if Order.checkIncreasing(list):
			return Order.INCREASING
		elif Order.checkDecreasing(list):
			return Order.DECREASING
		else: 
			return Order.UNORDERED