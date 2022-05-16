# informa se o triangulo é retangulo ou não


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def retangulo(self):
        if (self.a**2 + self.b**2) == self.c**2:
            return True
        else:
            return False


t = Triangulo(1, 3, 5)
t.retangulo()
