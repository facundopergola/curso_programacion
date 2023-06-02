class Vehiculo():
	def __init__(self, name, modelo, asientos, luces):
		self.name = name
		self.modelo = modelo

		self.asientos = asientos
		self.luces = luces

	def get_modelo(self):
		return self.modelo
	
	def get_name(self):
		return self.name

	def set_modelo(self, modelo):
		self.modelo = modelo
	
	def set_name(self, name):
		self.name = name

	#NUEVO
	def get_asientos(self):
		return self.asientos
	
	def set_asientos(self, asientos):
		self.asientos = asientos

	def get_luces(self):
		return self.luces
	
	def set_luces(self, luces):
		self.asientos = luces

class Avion(Vehiculo):
	
	def __init__(self, name, modelo, cantidadDeAlas):		
		super().__init__(name, modelo)
		self.cantidadDeAlas = cantidadDeAlas

	def despegar(self):
		print("despegando..")

#NUEVO	
class Avioneta(Avion):
	pass


class Barco(Vehiculo):
	def navegar(self):
		print("navegando..")

class Bote(Barco):
	pass


avion1 = Avion(modelo="747", name="el aguila blanca", cantidadDeAlas=2)
print(avion1.get_modelo())
avion1.despegar()


barco1 = Barco(modelo="Crucero", name="Titanic")
print(barco1.get_modelo())
barco1.navegar()

bote1 = Bote(name="bote chico", modelo="Titanico")
print(bote1.get_modelo())
bote1.navegar()

#NUEVO
class Auto(Vehiculo):
	def derrapar(self):
		print("derrapando")

