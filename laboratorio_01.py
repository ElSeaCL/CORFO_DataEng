#!/home/sebaegg/anaconda3/bin/python
# coding: utf-8

# ---
# 
# # Ejercicios curso intensivo de Python

# Cada pregunta tiene dos lineas, escriba la solución en la primera línea y compárela con el resultado de la segunda línea para ver si su respuesta es correcta.

# **1. Cuánto es 7 elevado a la potencia de 4?**
print('Ejercicio 1:')
print(7**4)
print('\n')

# **2. Calcule el factorial de 7**
# 
# Utilice el módulo math
print('Ejercicio 2:')
import math

print(math.factorial(7))
print('\n')

# **3. Dadas las siguientes variables**
# 
planet = "Earth"
diameter = 12742
# 
# **Use .format() para imprimir el siguiente string:**
# 
#     The diameter of Earth is 12742 kilometers.

print('Ejercicio 3:')
print('The diameter of {} is {} kilometers'.format(planet, diameter))
print('\n')

# **4. Cree una función que permita calcular el área de un círculo a partir del radio**
print('Ejercicio 4: Area de un circulo\n')

def area(radio):
    """
    Retorna el area de un circulo a partir del radio.
    """
    return math.pi * radio ** 2

print(area(1))
print(area(2))
print(area(4))
print('\n')

# **5. Cree una función que calcule el área de un triángulo. Realice pruebas.**
# 
# Recuerde que el área de un triángulo es igual al producto de la base por la altura dividido por 2.
# 
print('Ejercicio 5: Area de un triangulo')

def t(base,altura):
    """
    Calcula el area de un triangulo a partir de su base y altura.
    """
    return base * altura / 2

print(t(2,2))
print(t(4,4))
print('\n')

# **6. Cree una función que permita calcular la medida de la hipotenusa de un triángulo a partir de las medidas de los catetos**
print('Ejercicio 6: Hipotenusas a partir de sus catetos')

def h(cateto1, cateto2):
    """
    Obtiene la medida de la hipotenusa de un triangulo a partir del valor de
    respectivos catetos
    """

    return (cateto1**2 + cateto2**2)**0.5

print(h(3,4))
print('\n')

# **7. Cree una función "f" que retorne el cálculo de la siguiente fórmula. Haga pruebas.**
# 
# $$y=6x^{2}+3x+2$$
print('Ejercicio 7: Resultado de una funcion')

def f(x):
    return 6*x**2+3*x+2

print(f(2))
print(f(5))
print(f(20))
print(f(-20))
print('\n')

# **8. Cuando las ardillas se juntan para una fiesta, les gusta tener cigarros. Una fiesta de ardillas es exitosa cuando la cantidad de cigarros está entre 40 y 60, inclusive. 
# A menos que sea el fin de semana, en cuyo caso no hay límite superior en la cantidad de cigarros. 
# Implemente una función que devuelva True si se cumple la condición o caso contrario retorne False.**
print('Ejercicio 8: Fiesta de ardillas')

def cigar_party(cigars, isWeekend):
    """
    Devuelve True si cumple con las condiciones para ser una fiesta de ardillas exitosa.
    Retorna False en caso de que no lo sea.

    Argumentos:
        -cigars (int): Numero de cigarros que hay en la fiesta.
        -isWeekend (bool): True si es fin de semana.
    """

    esExitosa = False

    if cigars in range(40,61):
        esExitosa = True
    elif cigars >= 40 and isWeekend:
        esExitosa = True

    return esExitosa

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))
print(cigar_party(30, True))
print('\n')

# ### 9. Problema Final (El Jefe de la etapa)
# Estás manejando un poquito rápido por la carretera y la policía te detiene. Escribe 
# una función que retorne 3 posibles resultados: "Sin infracción", "Infracción Leve", 
# "Infracción Grave". Si su velocidad es 60 o menos km/h, el resultado es "Sin 
# Infracción". Si la velocidad está entre 61 y 80 inclusivo, el resultado es "Infracción 
# Leve". Si la velocidad es 81 o más, el resultado es "Infracción Grave". Pero si usted 
# estuviera de cumpleaños (valor booleano en la función), entonces usted puede ir 5 kms 
# por hora en todos los casos
print('Ejercicio 9: FINAL BOSS')

print('MENSAJE PARA EL PROFE: La descripcion del problema no deja claro que hacer')
print('en caso de cumpleanos, por lo que voy a ASUMIR que se puede manejar una velocidad')
print('5km mayor en todos los limites\n')

def caught_speeding(speed, is_birthday):
    """
    Retorna el resultado de una infraccion segun la velocidad en la que se iba.
    """
    limites = [60, 80]    

    if is_birthday:
        for i in range(2):
            limites[i] += 5
    
    if speed > limites[1]:
        infraccion = 'Infracción Grave'
    elif speed > limites[0]:
        infraccion = 'Infracción Leve'    
    else:
        infraccion = 'Sin Infracción'
        
    return infraccion

print(caught_speeding(81,True))
print(caught_speeding(81,False))

# # Buen Trabajo!
