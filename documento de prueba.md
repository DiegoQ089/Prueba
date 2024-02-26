import random

def generar_y_verificar_paridad():
    numero_aleatorio = random.randint(1, 100)
    
    if numero_aleatorio % 2 == 0:
        return f"El número aleatorio {numero_aleatorio} es par."
    else:
        return f"El número aleatorio {numero_aleatorio} es impar."

resultado = generar_y_verificar_paridad()
print(resultado)


# Imprimir un mensaje en la consola
print("Hola, mundoooooooo!")

# Sumar dos números
numero1 = 10
numero2 = 20
numero3 = 300000
suma = numero1 + numero2 + numero3

# Imprimir el resultado de la suma
print("La suma de ", numero1, " y ", numero2, " y " , numero3 , " es ", suma)

# Pedir un nombre al usuario
nombre = input("¿Cómo te llamas? ")

# Saludo personalizado
print("¡Hola", nombre, "!")
