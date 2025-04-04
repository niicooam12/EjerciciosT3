naves = [
    {"nombre": "Cometa Veloz", "longitud": 50, "tripulantes": 4, "pasajeros": 6},
    {"nombre": "Titán del Cosmos", "longitud": 55, "tripulantes": 6, "pasajeros": 7},
    {"nombre": "nave1", "longitud": 45, "tripulantes": 4, "pasajeros": 5},
    {"nombre": "nave2", "longitud": 60, "tripulantes": 5, "pasajeros": 4},
    {"nombre": "nave3", "longitud": 50, "tripulantes": 4, "pasajeros": 6},
    {"nombre": "nave4", "longitud": 48, "tripulantes": 5, "pasajeros": 5},
    {"nombre": "nave5", "longitud": 59, "tripulantes": 6, "pasajeros": 7},
    {"nombre": "nave6", "longitud": 40, "tripulantes": 3, "pasajeros": 3},
    {"nombre": "GXnave7", "longitud": 45, "tripulantes": 4, "pasajeros": 5},
    {"nombre": "nave8", "longitud": 52, "tripulantes": 5, "pasajeros": 6},
]

# Ordenar naves por nombre y longitud descendente
naves_ordenadas = sorted(naves, key=lambda x: (x["nombre"], -x["longitud"]))
print("Naves ordenadas por nombre y longitud:")
for nave in naves_ordenadas:
    print(nave)

# Filtrar naves seleccionadas
seleccion_naves = {"Cometa Veloz", "Titán del Cosmos"}
print("\nNaves seleccionadas:")
for nave in naves:
    if nave["nombre"] in seleccion_naves:
        print(nave)

# Top 5 naves con más pasajeros
naves_pasajeros_top5 = sorted(naves, key=lambda nave: nave['pasajeros'], reverse=True)[:5]
print("\nTop 5 naves con más pasajeros:")
for nave in naves_pasajeros_top5:
    print(nave)

# Nave con más tripulantes
nave_mas_tripulantes = max(naves, key=lambda nave: nave['tripulantes'])
print("\nNave con más tripulantes:")
print(nave_mas_tripulantes)

# Naves cuyo nombre empieza con "GX"
naves_gx = [nave for nave in naves if nave["nombre"].startswith("GX")]
print("\nNaves cuyo nombre empieza con 'GX':")
for nave in naves_gx:
    print(nave)

# Naves con 6 o más tripulantes
naves_6_tripulantes = [nave for nave in naves if nave["tripulantes"] >= 6]
print("\nNaves con 6 o más tripulantes:")
for nave in naves_6_tripulantes:
    print(nave)

# Nave más pequeña y más grande por longitud
nave_pequena = min(naves, key=lambda nave: nave["longitud"])
nave_grande = max(naves, key=lambda nave: nave["longitud"])
print("\nNave más pequeña:")
print(nave_pequena)
print("\nNave más grande:")
print(nave_grande)