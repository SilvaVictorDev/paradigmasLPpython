# Procedural Paradigm
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
print("Fatorial de 5 (Procedural): ", fatorial(5))

# Object-Oriented Paradigm
class Fatorial:
    def calculate(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate(n -1)
f = Fatorial()
print("Fatorial de 5 (orientado a objetos) :", f.calculate(5))
