import math

def calculadora_raiz_cuadrada():
    while True:
        numero = float(input("Introduce un número: "))
        if numero < 0:
            print("Error: no se puede calcular la raíz cuadrada de un número negativo.")
        else:
            raiz_cuadrada = math.sqrt(numero)
            print(f"La raíz cuadrada de {numero} es {raiz_cuadrada:.2f}")

calculadora_raiz_cuadrada()