import math

class Radianes:
    def __init__(self, valor):
        self.valor = valor

    def a_grados(self):
        return self.valor * (180 / math.pi)

class Grados:
    def __init__(self, valor):
        self.valor = valor

    def a_radianes(self):
        return self.valor * (math.pi / 180)