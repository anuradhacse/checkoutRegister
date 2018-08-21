"""This is the product class. It has properties name, weight(In Kg) and price(AUD)"""
class Product(object):
  
	def __init__(self, name, weight, price, barcode):
		self.name = name
		self.weight = weight
		self.price = price
		self.barcode = barcode

	def set_weight(self, weight=0.0):
		self.weight = weight

	def get_weight(self):
		return self.weight


	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_barcode(self, barcode):
		self.barcode = barcode

	def get_barcode(self):
		return self.barcode

