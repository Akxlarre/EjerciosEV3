#import
import numpy as np
import os
'''
Ejercicio 1
    Declarar y poblar un arreglo unidimensional de largo 10 con números enterospositivos, 
    utilizando la función random, luego ingrese un número e indique si éste seencuentra en el arreglo
'''
arreglo = np.random.randint(1,100,10)
print(arreglo)
numero = int(input("Ingrese un numero: "))
encontrado = False
for i in range(len(arreglo)):
    if numero == arreglo[i]:
        encontrado = True
        break
if encontrado == True:
    print("El numero esta en el arreglo")
else:
    print("El numero no esta en el arreglo")

'''
Ejercicio 2
    Ingresar dos números enteros positivos entre 3 y 6, ambos inclusive,
    luego esos números serán las dimensiones de un arreglo bidimensional. Posteriormente,
    poblar la matriz con números reales. Finalmente, muestre:
        •El arreglo poblado.
        •La suma por filas.
        •El promedio por columnas.
'''


filas = int(input("Ingrese el numero de filas entre 3 y 6: "))
columnas = int(input("Ingrese el numero de columnas entre 3 y 6: "))
arregloBidimensional = np.random.randint(1,100,(filas,columnas))
print(arregloBidimensional)
sumaFilas = arregloBidimensional.sum(axis=1)
print(sumaFilas)
promedioColumnas = arregloBidimensional.mean(axis=0)
print(promedioColumnas)

'''
Ejercicio 3
Crear un programa que contenga un menú con las siguientes opciones:
• Área de un circulo
• Perímetro de un cuadrado
Ingrese los valores necesarios para calcular y entregar resultados utilizando funciones.
'''

PI = 3.1416
def areaCirculo(radio):
    area = PI * radio**2
    return area;
def perimetroCuadrado(lado):
    perimetro = lado * 4
    return perimetro;

while True:
    try:
        print("1. Area de un circulo")
        print("2. Perimetro de un cuadrado")
        print("3. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            radio = float(input("Ingrese el radio del circulo: "))
            print(f"El area del circulo es: {areaCirculo(radio)}")
        elif opcion == 2:
            lado = float(input("Ingrese el lado del cuadrado: "))
            print(f"El perimetro del cuadrado es: {perimetroCuadrado(lado)}")
        elif opcion == 3:
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Ingrese un numero") 

'''Ejercicio 4
En una cafetería se venden 4 tipos de cafés:
• Espresso $1.500
• Capuchino $1.800
• Latte $1.600
• Moca $1.700
Determine el total a pagar por un cliente que puede llevar varios cafés y 
aplique eldescuento del 10% al total a pagar, si su compra es superior o igual a $3.000.
Considere crear un menú de opciones y calcule el monto utilizando función '''
def precio_por_cantidad(precio_unitario, cantidad):
    total = precio_unitario * cantidad     
    return total;

def aplicacion_descuento(total):
    if total_acumulado >= 3000:
        return total_acumulado - total_acumulado * 0.1 
    else:
        return total_acumulado
total_acumulado = 0
Espresso = 1500
Capuchino = 1800
Latte = 1600
Moca = 1700

while True:
    try:
        print('''tipos de cafés:
            1-Espresso $1.500
            2-capuchino $1.800
            3-Latte $1.600
            4-Moca $1.700
            5-Salir''')
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            cantidad = int(input("Ingrese la cantidad: "))
            total = precio_por_cantidad(Espresso, cantidad)
            total_acumulado += total
        elif opcion == 2:
            cantidad = int(input("Ingrese la cantidad: "))
            total = precio_por_cantidad(Capuchino, cantidad)
            total_acumulado += total
        elif opcion == 3:
            cantidad = int(input("Ingrese la cantidad: "))
            total = precio_por_cantidad(Latte, cantidad)
            total_acumulado += total
        elif opcion == 4:
            cantidad = int(input("Ingrese la cantidad: "))
            total = precio_por_cantidad(Moca, cantidad)
            total_acumulado += total
        elif opcion == 5:
            print(f"El total a pagar es: {aplicacion_descuento(total_acumulado)}")
            break
    except ValueError:
        print("digite un numero")
    