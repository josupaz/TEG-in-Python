import math

class Punto:
    cuadrante = 0
    
    def __init__ (self,ejeX=0,ejeY=0):
        self.ejeX=ejeX
        self.ejeY=ejeY

    def __str__(self):
        return "x = {} y = {} ".format(self.ejeX,self.ejeY)

    def mostrar_cuadrante(self):
        if(self.ejeX > 0 and self.ejeY > 0):
             self.cuadrante = 1
        elif (self.ejeX < 0 and self.ejeY > 0):
            self.cuadrante = 2
        elif(self.ejeX < 0 and self.ejeY < 0):
            self.cuadrante = 3
        elif(self.ejeX > 0 and self.ejeY < 0):
            self.cuadrante = 4
        else:
            self.cuadrante = 0
        
        print("Pertenece al cuadrante {}".format(self.cuadrante))

    def vector(self,p):
        x = int(p.ejeX - self.ejeX)
        y = int(p.ejeY - self.ejeY)

        print("Vector es: {} {}".format(x,y))
        return x, y

    def distancia(self,p):
         x, y = self.vector(p)
         d = math.sqrt(x**2 + y**2)
         print("distncia entre los puntos: {}".format(d))

a = Punto(2,3)
b = Punto(5,5)
c = Punto(-3,-1)
d = Punto(0,0)

print("Punto 1------------")
print("A = ",a)
print("B = ",b)
print("C = ",c)
print("D = ",d)

print("Punto 2------------")
a.mostrar_cuadrante()
b.mostrar_cuadrante()
d.mostrar_cuadrante()

print("Punto 3------------")
a.vector(b)
b.vector(a)

print("Punto 4------------")

a.distancia(b)
b.distancia(a)

print("Punto 5------------")

