# hacer una clase que contenga las operaciones aritmeticas basicas definiendo a y b como atributos
import os
os.system('cls' if os.name == 'nt' else 'clear')

class OperacionesAritmeticas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        print (self.a + self.b)

    def potencia(self):
        print (self.a ** self.b)

op = OperacionesAritmeticas(int(input("ingrese valor para a: ")), int(input("ingrese valor para b: ")))
op.suma()

potencia = int(input("ingrese valor para a: "))
potencia = int(input("ingrese valor para b: "))

print("La potencia de a es ", potencia ** potencia)

op.potencia()