#1

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

