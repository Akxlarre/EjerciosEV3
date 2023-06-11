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


    
    