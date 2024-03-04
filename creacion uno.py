def fibonacci(n):
    fib_lista = [0, 1]
    for _ in range(2, n):
        siguiente_numero = fib_lista[-1] + fib_lista[-2]
        fib_lista.append(siguiente_numero)
    return fib_lista

resultado = fibonacci(10)
print("Los primeros diez números de la serie de Fibonacci son:", resultado)


print("Esto es una prueba1")
print("Esto es una prueba2")
print("Esto es una prueba3")
print("Esto es una prueba8")

