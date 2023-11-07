def división(num1, num2):
    if num2 == 0:
        print("ERROR! Imposible dividir entre 0.")
    else:
        resultado = num1/num2
    return resultado

def main():
    num1 = float(input("Introduzca un número: "))
    num2 = float(input("Introduzca otro: "))

    print(f"El resultado de la división es {resultado}")

if __name__ == "__main__":
    main()