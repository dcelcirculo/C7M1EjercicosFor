# Imprimir las 10 tabals de multiplicar
tabla = 1

for x in range(1,11):
    print(f"Tabla del {x}")
    for y in range(1, 11):
        print(f"{y} * {tabla} = {y * tabla}")
    tabla += 1
