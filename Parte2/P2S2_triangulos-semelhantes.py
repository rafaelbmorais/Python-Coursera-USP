# informa se o triangulo é retangulo ou não


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def semelhantes(self, t2):

        if ((self.a/t2.a) == (self.b / t2.b)) and ((self.a/t2.a) == (self.c / t2.c)):
            return True
        else:
            return False

t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
t1.semelhantes(t2)
