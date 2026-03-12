"""
Escriba un programa que pida al ususario 2 numeros y uestre un menu de opciones
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo
8. Salir
"""

def suma(a, b):
    suma = a + b
    return suma

def resta(a, b):
    resta = a - b
    return resta

def multiplicacion(a, b):
    multiplicacion = a * b
    return multiplicacion

def division(a, b):
    division = a / b
    return division

def div_entera(a, b):
    div_entera = a // b
    return div_entera

def potencia(a, b):
    potencia = pow(a, b)
    return potencia

def modulo(a, b):
    modulo = a % b
    return modulo


a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el primer numero: "))

menu = """
Escoja una opcion:
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo
8. Salir
"""

opcion = 0
while opcion != 8:
    print(menu)
    opcion = int(input("Escoja una opcion: "))
    if opcion == 1:
        print(f"El resultado de la suma es = {suma(a, b)}")
    elif opcion == 2:
        print(f"El resultado de la resta es = {resta(a, b)}")
    elif opcion == 3:
        print(f"El resultado de la resta es = {multiplicacion(a, b)}")
    elif opcion == 4:
        print(f"El resultado de la division es = {division(a, b)}")
    elif opcion == 5:
        print(f"El resultado de la division entera es = {div_entera(a, b)}")
    elif opcion == 6:
        print(f"El resultado de la potencia es = {potencia(a, b)}")
    elif opcion == 7:
        print(f"El resultado del modulo es = {modulo(a, b)}")
    elif opcion == 8:
        print("Gracias por usar nuestra calculadora.")
        break
    else:
        print("Opcion no valida")


