class CarritoDeComida():
	def __init__(self, name, modelo, ruedas ,publicidad):
		self.name = name
		self.modelo = modelo
		self.ruedas = ruedas
		self.publicidad = publicidad
	
	def get_name(self):
		return self.name
	
	def get_modelo(self):
		return self.modelo
	
	def get_ruedas(self):
		return self.ruedas

	def get_publicidad(self):
		return self.publicidad


carrito1 = CarritoDeComida(name="Elpancholoco",
			    modelo="Furgon",
			    ruedas=4,
			     publicidad="Los mejores Panchos Del condado!")

print(carrito1.get_name())
print(carrito1.get_modelo())