class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def calcular_determinante_recursivo(self):
        return self.determinante_recursivo(self.matriz)

    def determinante_recursivo(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            return "La matriz debe ser de 3x3"
        
        # Fórmula para el determinante de una matriz 3x3
        return (
            matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) -
            matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) +
            matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])
        )

    def calcular_determinante_iterativo(self):
        return self.determinante_iterativo(self.matriz)

    def determinante_iterativo(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            return "La matriz debe ser de 3x3"
        
        # Cálculo iterativo del determinante de una matriz 3x3
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]

        determinante = (
            a * (e * i - f * h) -
            b * (d * i - f * g) +
            c * (d * h - e * g)
        )
        return determinante