

class Motocicleta():
    estado = "nueva"
    motor = False
    numero_ruedas = 2
    capacidad_tanque = 40
    luces = False

 
    # metodo constructor
    def __init__(self,color,matricula,combustible,marca,modelo,fecha_fabricacion,velocidad_punta,peso):
        # attributos
        self.color = color
        self.matricula = matricula
        self.combustible = combustible
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso

        
    def arrancar(self):
        if self.motor == False and self.combustible > 0:
            self.motor  = True
            print("el motor arranco")
        else:
            print("el motor ya estaba en marcha or no tengo combustible disponible")

    def detener(self):
        if self.motor == True:
            self.motor = False
            print("el motor se detuvo")
        else:
            print("el motor ya estaba apagado")
    
    def andar(self):
        if self.motor == True:
            print("La motocicleta esta encendida")
            print("chequeando combustible...")
            if self.combustible > 0:
                print("combustible OK")
                self.combustible = self.combustible - 1
            else:
                  print("combustible insuficiente")
                  self.motor = False
        else:
              print("el motor esta apagado")
            
            
    def get_combustible(self):
        return self.combustible
    
    def set_combustible(self, lts):
        self.combustible = lts
            
    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color
        
    def esta_encendida(self):
        if self.motor == True:
            print("La motocicleta esta encendida")
        else:
            print("La motocicleta NO esta encendida")

    def get_luces(self):
        if self.luces == True:
            print("Las luces estan encendidas")
        else:
            print("las luces estan apagadas")


motocicleta_yamaha_1 = Motocicleta(
matricula="6432-YHUZ",
combustible=3,
color="Negra",
marca="Yamaha",
modelo="Ybr 125",
peso=320,
fecha_fabricacion="29/09/2019",
velocidad_punta=165)



motocicleta_yamaha_1.arrancar()
motocicleta_yamaha_1.esta_encendida()
motocicleta_yamaha_1.andar()
motocicleta_yamaha_1.andar()
motocicleta_yamaha_1.andar()
motocicleta_yamaha_1.andar()
print(motocicleta_yamaha_1.get_combustible())
motocicleta_yamaha_1.esta_encendida()












