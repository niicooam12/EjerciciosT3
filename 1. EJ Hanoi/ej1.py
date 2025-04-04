class TorreHanoi:
    def __init__(self, num_piedras):
        self.num_piedras = num_piedras

    def resolver(self, n, origen, destino, auxiliar):
        if n == 1:
            print(f"Mueve la piedra de {origen} a {destino}")
            return
        # Mueve n-1 piedras de la columna origen a la columna auxiliar
        self.resolver(n - 1, origen, auxiliar, destino)
        # Mueve la piedra más grande de la columna origen a la columna destino
        print(f"Mueve la piedra de {origen} a {destino}")
        # Mueve las n-1 piedras de la columna auxiliar a la columna destino
        self.resolver(n - 1, auxiliar, destino, origen)

    def iniciar(self):
        self.resolver(self.num_piedras, "Columna A", "Columna B", "Columna C")

num_piedras = int(input("Ingrese el número de piedras: "))

torre_hanoi = TorreHanoi(num_piedras)
torre_hanoi.iniciar()