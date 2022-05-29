"""
Realizar una función llamada año_bisiesto:
Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número debe indicar que se ingrese un número.
Información a tener en cuenta al realizar el entregable:
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
"""

# Defino la funcion año biciesto
def año_bisiesto():
  # Le pido que intente avanzar, y que pida un número
  try:
    anho=int(input("Ingrese un año para saber si es bisiesto: "))

    # Preparo las respuestas "es" y "no es" bisiesto, para luego llamar en los print a estas funciones y escribir menos.
    es=f"El año {anho} es bisiesto."
    no_es=f"El año {anho} no es bisiesto."

    # Verifico que sea un número mayor a 0
    if anho>0:

      # Si es múltiplo de 4
      if anho%4==0:

        # Si es múltiplo de 4 y de 100
        if anho%100==0:
          
          # Si es múltiplo de 4, de 100 y de 400
          if anho%400==0:
            return print(es)

          # Si es múltiplo de 4, de 100 y no es múltiplo de 400
          else:
            return print(no_es)

        # Si es múltiplo de 4 y no es múltiplo de 100
        else:
          return print(es)

      # Si no es múltiplo de 4
      else:
        return print(no_es)  

    # Si el año no es mayor que 0:
    else:
      # Mensaje de error
      print(f"El año ingresado no es mayor que 0. Intenta nuevamente.")
      # Llamo de nuevo la función.
      return año_bisiesto() 

  # Si el dato ingresado no es un número.
  except:
    # Mensaje de error
    print("No ingresaste un número. Intenta de nuevo.")
    # Llamo de nuevo la función.
    año_bisiesto()

  return

#Llama a la función.
año_bisiesto()
