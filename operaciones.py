def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    resultado_suma = sumar(5, 3)
    resultado_resta = restar(8, 2)
    resultado_multiplicacion = multiplicar(4, 6)
    resultado_division = dividir(10, 2)

    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Multiplicación: {resultado_multiplicacion}")
    print(f"División: {resultado_division}")