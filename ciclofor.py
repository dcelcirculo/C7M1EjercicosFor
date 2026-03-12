# Imprimir las 10 tabals de multiplicar
tabla = 1

for x in range(1,11):
    for y in range(1, 11):
        print(f"{y} * {tabla} = {y * tabla}")
    print(f"Tabla del {x}")
    tabla += 1
