# Ejercicio 1: Imprimir números del 0 al 100
print("Números del 0 al 100:")
for i in range(101): 
  print(i)

# Ejercicio 2: Contar dígitos de un numero

numero = int(input("Ingresa un numero:"))
i = 0

while numero > 0:
  numero = numero // 10
  i += 1
print(f"El numero tiene {i} digitos")


# Ejercicio 3: Sumar números entre dos valores (excluidos)
def suma_entre_valores():
    try:
        inicio = int(input("Introduce el primer número entero: "))
        fin = int(input("Introduce el segundo número entero: "))

        # Asegurarse de que inicio sea menor que fin
        if inicio > fin:
            inicio, fin = fin, inicio

        suma = 0
        for num in range(inicio + 1, fin):
            suma += num

        print(f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}")

    except ValueError:
        print("Por favor, introduce valores enteros válidos.")

# Ejecutamos la función
suma_entre_valores()

# Ejercicio 4: Sumar números hasta ingresar 0
suma_total = 0
print("Ingrese números enteros (ingrese 0 para terminar):")

while True:
  try:
    numero_str = input("Ingrese un número: ")
    numero = int(numero_str)

    if numero == 0:
      break # Salir del bucle si el número es 0
    else:
      suma_total += numero
  except ValueError:
    print("Entrada inválida. Por favor ingrese un número entero.")


print(f"La suma total es: {suma_total}")


# Ejercicio 5: Juego de adivinar el número
import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("¡Adivina el número secreto entre 0 y 9!")

while not adivinado:
  try:
    intento_usuario_str = input("Ingresa tu intento: ")
    intento_usuario = int(intento_usuario_str)
    intentos += 1

    if intento_usuario == numero_secreto:
      print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
      adivinado = True
    elif intento_usuario < 0 or intento_usuario > 9:
       print("El número debe estar entre 0 y 9.")
    elif intento_usuario < numero_secreto:
      print("Incorrecto. El número secreto es mayor. Intenta de nuevo.")
    else: # intento_usuario > numero_secreto
      print("Incorrecto. El número secreto es menor. Intenta de nuevo.")

  except ValueError:
    print("Entrada inválida. Por favor ingrese un número entero.")


print(f"Necesitaste {intentos} intento(s).")

# Ejercicio 6: Imprimir pares entre 0 y 100 (decreciente)
print("Números pares del 100 al 0:")
for i in range(100, -1, -2): # Empieza en 100, hasta 0, paso -2
  print(i)




  # Ejercicio 7: Suma hasta un número positivo dado
try:
  limite_str = input("Ingrese un número entero positivo: ")
  limite = int(limite_str)
  suma = 0

  if limite < 0:
    print("El número debe ser positivo.")
  else:
    # range(limite + 1) va de 0 hasta limite (incluido)
    for i in range(limite + 1):
      suma += i
    print(f"La suma desde 0 hasta {limite} es: {suma}")

except ValueError:
  print("Entrada inválida. Por favor ingrese un número entero.")



  # Ejercicio 8: Contar tipos de números
# Cambia este valor para probar con menos números
cantidad_numeros = 5 # Originalmente 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
  while True: # Bucle para reintentar si la entrada no es válida
    try:
      numero_str = input(f"Ingrese el número {i + 1}: ")
      numero = int(numero_str)

      # Contar pares e impares
      if numero % 2 == 0:
        pares += 1
      else:
        impares += 1

      # Contar positivos y negativos (0 no es ni positivo ni negativo)
      if numero > 0:
        positivos += 1
      elif numero < 0:
        negativos += 1

      break # Salir del bucle de reintento si el número es válido
    except ValueError:
      print("Entrada inválida. Por favor ingrese un número entero.")


print("\n--- Resultados ---")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números cero: {cantidad_numeros - (positivos + negativos)}")



# Ejercicio 9: Calcular la media de N números
# Cambia este valor para probar con menos números
cantidad_numeros = 5 # Originalmente 100

suma_total = 0.0 # Usar float para la suma y la media

print(f"Ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
  while True: # Bucle para reintentar si la entrada no es válida
    try:
      numero_str = input(f"Ingrese el número {i + 1}: ")
      numero = int(numero_str)
      suma_total += numero
      break # Salir del bucle de reintento si el número es válido
    except ValueError:
      print("Entrada inválida. Por favor ingrese un número entero.")


# Calcular la media, evitando división por cero
if cantidad_numeros > 0:
  media = suma_total / cantidad_numeros
  print(f"\nLa suma total es: {suma_total}")
  print(f"La media de los {cantidad_numeros} números es: {media}")
else:
  print("\nNo se ingresaron números para calcular la media.")




  # Ejercicio 10: Invertir dígitos de un número
try:
  numero_str = input("Ingrese un número entero para invertir: ")
  numero = int(numero_str)
  numero_original = numero # Guardar para mostrar al final

  numero_invertido = 0
  es_negativo = False

  # Manejar negativos
  if numero < 0:
    es_negativo = True
    numero = abs(numero)

  # Invertir los dígitos
  temp_numero = numero
  while temp_numero > 0:
    digito = temp_numero % 10
    numero_invertido = (numero_invertido * 10) + digito
    temp_numero //= 10 # División entera

  # Si era negativo, añadir el signo al resultado
  if es_negativo:
    numero_invertido *= -1

  print(f"El número {numero_original} invertido es: {numero_invertido}")

except ValueError:
  print("Entrada inválida. Por favor ingrese un número entero.")