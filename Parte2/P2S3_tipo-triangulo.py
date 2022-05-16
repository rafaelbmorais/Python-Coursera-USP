# devolve uma string informando se o trinagulo é isosceles, equilatero ou escaleno.

def main():
    t = Triangulo(3, 4, 5)
    t.tipo_lado()

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return ('equilátero')
        elif ((self.a == self.b) and (self.a != self.c)) or ((self.a == self.c) and (self.a != self.b)) or ((self.b == self.c) and (self.b != self.a)):
            return ('isósceles')
        else:
            return ('escaleno')

main()
