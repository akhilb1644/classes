from random import randint

class Car:
	def __init__(self,_make,_model,_year,_owner,_odometer_read):
		self._make = _make
		self._model = _model
		self._year = _year
		self._owner = _owner
		self._odometer_read = _odometer_read
		
	def __repr__(self):
		return "The %s %s was made in %s and is currently owned by %s" % (self._make,self._model,self._year,self._owner)
	
class GasCar(Car):
	def __init__(self,_make,_model,_year,_owner,_odometer_read,_gallon_capacity,_mpg):
		super().__init__ (make,model,year,owner,_odometer_read)
		self._gallons = _gallon_capacity
		self._mpg = _mpg
		self._odometer_read = 0
		
	def _fillGas(self):
		self._gallons = _gallon_capacity
	
	def _useGas(self,method):
		distance = method(miles)
		gas_used = mpg / distance
		return gas_used
	
	@_useGas
	def drive(self,miles):
		self._odometer_read += miles
		return miles
