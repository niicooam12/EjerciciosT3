class Nave:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __repr__(self):
        return f"Nave(nombre={self.nombre}, longitud={self.longitud}, tripulantes={self.tripulantes}, pasajeros={self.pasajeros})"


class Flota:
    def __init__(self, naves):
        self.naves = naves

    def ordenar_por_nombre_y_longitud(self):
        return sorted(self.naves, key=lambda x: (x.nombre, -x.longitud))

    def filtrar_por_nombres(self, nombres_seleccionados):
        return [nave for nave in self.naves if nave.nombre in nombres_seleccionados]

    def top_naves_por_pasajeros(self, top=5):
        return sorted(self.naves, key=lambda nave: nave.pasajeros, reverse=True)[:top]

    def nave_con_mas_tripulantes(self):
        return max(self.naves, key=lambda nave: nave.tripulantes)

    def naves_con_nombre_gx(self):
        return [nave for nave in self.naves if nave.nombre.startswith("GX")]

    def naves_con_tripulantes_mayores_a(self, cantidad):
        return [nave for nave in self.naves if nave.tripulantes >= cantidad]

    def nave_mas_pequena_y_grande(self):
        nave_pequena = min(self.naves, key=lambda nave: nave.longitud)
        nave_grande = max(self.naves, key=lambda nave: nave.longitud)
        return nave_pequena, nave_grande


# Crear las naves
naves = [
    Nave("Cometa Veloz", 50, 4, 6),
    Nave("Titán del Cosmos", 55, 6, 7),
    Nave("nave1", 45, 4, 5),
    Nave("nave2", 60, 5, 4),
    Nave("nave3", 50, 4, 6),
    Nave("nave4", 48, 5, 5),
    Nave("nave5", 59, 6, 7),
    Nave("nave6", 40, 3, 3),
    Nave("GXnave7", 45, 4, 5),
    Nave("nave8", 52, 5, 6),
]

# Crear la flota
flota = Flota(naves)

# Ordenar naves por nombre y longitud descendente
print("Naves ordenadas por nombre y longitud:")
for nave in flota.ordenar_por_nombre_y_longitud():
    print(nave)

# Filtrar naves seleccionadas
seleccion_naves = {"Cometa Veloz", "Titán del Cosmos"}
print("\nNaves seleccionadas:")
for nave in flota.filtrar_por_nombres(seleccion_naves):
    print(nave)

# Top 5 naves con más pasajeros
print("\nTop 5 naves con más pasajeros:")
for nave in flota.top_naves_por_pasajeros():
    print(nave)

# Nave con más tripulantes
print("\nNave con más tripulantes:")
print(flota.nave_con_mas_tripulantes())

# Naves cuyo nombre empieza con "GX"
print("\nNaves cuyo nombre empieza con 'GX':")
for nave in flota.naves_con_nombre_gx():
    print(nave)

# Naves con 6 o más tripulantes
print("\nNaves con 6 o más tripulantes:")
for nave in flota.naves_con_tripulantes_mayores_a(6):
    print(nave)

# Nave más pequeña y más grande por longitud
nave_pequena, nave_grande = flota.nave_mas_pequena_y_grande()
print("\nNave más pequeña:")
print(nave_pequena)
print("\nNave más grande:")
print(nave_grande)