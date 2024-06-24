import os
os.system('cls' if os.name == 'nt' else 'clear')

class Personaje:
    def __init__(self, nombre, arma):
        self.nombre = nombre
        self.arma = arma
class Mago(Personaje):
    pass

hechicero = Mago("Merlín","caldero")

print(hechicero.nombre)