#1
"""
1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.
"""

#Defino la función
def area_rectangulo(base, altura):
  # Defino como se calcula el área
  return base*altura
  
#Ingreso los datos dados
base=15
altura=10

# Llamo la funcion con los argumentos indicados
area=area_rectangulo(base, altura)

# Imprimo la respuesta
print(f"El área de un rectángulo de base {base} y altura {altura} es {area}")

#2
"""
2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.
"""

# Importo pi
import math
#print(math.pi)


#Defino la función
def area_circulo(radio):

  # Defino como se calcula el área
  return math.pi*(radio**2)
  
#Ingreso los datos dados
radio=5

# Llamo la función con el argumento indicado
area=area_circulo(radio)

# Imprimo la respuesta
print(f"El área de un círculo de radio {radio} es {area}")



#3
"""
3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1. Si el primer número es menor que el segundo, debe devolver -1. Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
"""

#Defino la función
def relacion(n1, n2):
  #Establezco las condiciones y resultados:
  if n1>n2:
    return print("La relación es 1.")
  if n1<n2:
    return print("La relación es -1.")
  if n1==n2:
    return print("La relación es 0.")
  
# Pido que se ingresen los dos números
n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese otro número: "))

# Llamo a la función para evaluar la relación entre los números
relacion(n1, n2)


#4
"""
4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24
"""

#Defino la función
def intermedio(n1, n2):
  # Defino como se calcula el punto intermedio
  return (n1+n2)/2
  
# Pido que se ingresen los dos números
n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese otro número: "))

# Llamo a la función y lo guardo en una variable
punto=int(intermedio(n1, n2))

# Imprimo la respuesta
print(f"El punto intermedio entre {n1} y {n2} es {punto}.")


#5
"""
5) Realizá una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste

Devolver el límite superior si el número es mayor que éste.

Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10
"""


#Defino la función
def recortar(rec, inf, sup):
  # Establezco las reglas y los resultados correspondientes
  if rec<inf:
    return print(inf)
  if rec>sup:
    return print(sup)
  if rec>inf and rec<sup:
    return print(rec)
    
  
# Pido que se ingresen los tres números
rec=int(input("Ingrese un número a recortar: "))
inf=int(input("Ingrese el límite inferior: "))
sup=int(input("Ingrese el límite superior: "))

# Llamo a la función para que devuelva el resultado
recortar(rec, inf, sup)




#6
"""
6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()
"""

# Defino la función separar()
def separar(original):
  # Preparo la lista de pares:
  pares=[]
  # Preparo la lista de impares:
  impares=[]
  # Coloco cada valor de la lista original en la lista correspondiente
  for x in original:
    if x%2==0:
      pares.append(x)
    else:
      impares.append(x)
  # Ordeno las 2 listas
  pares.sort()
  impares.sort()
  # Imprimo las dos listas
  print(f"La lista de números pares, ordenados de menor a mayor, ingresados en la lista original es {pares}")
  print(f"La lista de números impares, ordenados de menor a mayor, ingresados en la lista original es {impares}")



# Creo la lista original vacía
original=[]

# Creo una variable que sea True mientras se están agregando datos a la lista original, y que cambie a False cuando ya no se quieran ingresar mas números
agregar=True
while agregar==True:
  # voy agregando datos
  entrada=input("Ingrese un número entero para agregar a la lista, o ingrese \"s\" para salir: ")
  # Si no quieren cargar más números:
  if entrada=="s":
    agregar=False
  # Si quieren cargar más números:
  else:
    # Que intente si son números
    try:
      # Transforma el string en int
      entero=int(entrada)
      # Agrega el int a la lista original
      original.append(entero)
    # Si no ingresaron ni una s ni un número:
    except:
      # Le devuelvo un mensaje de error
      print("El dato ingresado no es correcto. Por favor, inténtelo nuevamente.")
      pass

# Llamo a la función
separar(original)

