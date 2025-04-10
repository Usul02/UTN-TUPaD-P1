#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, #deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_ejer1 = input("Ingrese su edad por favor:")
edad_ejer1 = int(edad_ejer1)
if edad_ejer1 >= 18:
    print("Eres mayor de edad")



# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota_aprobada = 6
nota_alumno = int(input("ingrese su nota:"))
if nota_alumno >= nota_aprobada:
 print ("Aprobado.")
else:
 print("Desaprobado")


#) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par"

numero_usuario = int(input("Ingrese un numero: "))
if numero_usuario % 2 == 0:
    print(f"Ha ingresado un número par:{numero_usuario}")
else:
    print("Por favor, ingrese un numero par")


#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#Adulto/a: mayor o igual que 30 años.

edad_ejer3 = int(input("Ingrese su edad: "))

if edad_ejer3 < 0:
  print("Error: La edad no puede ser negativa.")
elif edad_ejer3 < 12:
  print("Eres un niño/a")
elif edad_ejer3 < 18:
  print("Eres un adolescente")
elif edad_ejer3 < 30:
  print("Eres un adulto/a joven")
else:
  print("Eres un adulto/a")


# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".


#Solicitar la contraseña al usuario.
contraseña_usuario = input("Introduzca una contraseña: ")

longitud = len(contraseña_usuario)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    #Si la longitud está fuera del rango permitido, imprimir el mensaje de error.
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


#6)
import random
import statistics

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

promedio = statistics.mean(numeros_aleatorios)
print(f"La media es: {promedio}")

moda = statistics.mode(numeros_aleatorios)
print(f"La moda es: {moda}")

mediana = statistics.median(numeros_aleatorios)
print(f"La mediana es: {mediana}")


#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

texto = input("Ingresa una frase o palabra: ")


if texto[-1].lower() in 'aeiou':
    texto += '!' 

print("Resultado:", texto)


#8)
# Solicitar al usuario su nombre
nombre = input("Ingresa tu nombre: ")


print("¿Cómo quieres ver tu nombre?")
print("1. En MAYÚSCULAS")
print("2. En minúsculas")
print("3. Con la Primera Letra en Mayúscula")

opcion = input("Ingresa 1, 2 o 3: ")

if opcion == "1":
    print("Tu nombre en mayúsculas:", nombre.upper())
elif opcion == "2":
    print("Tu nombre en minúsculas:", nombre.lower())
elif opcion == "3":
    print("Tu nombre con la primera letra en mayúscula:", nombre.title())
else:
    print("Opción no válida.")


#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

# Solicita al usuario la magnitud del terremoto
magnitud = float(input("Introduce la magnitud del terremoto: "))

# Clasificación según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:  # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala).")



#10)
# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print("Estás en:", estacion)




