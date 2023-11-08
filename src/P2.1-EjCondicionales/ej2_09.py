def entrada(edad):
    if edad < 4:
        print("Usted entra gratis.")
    elif edad >= 4 and edad <18:
        print("El precio de la entrada es de 5€.")
    elif edad >= 18:
        print("El precio de la entrada es de 10€.")


def main():
    edad = int(input("Indique su edad: "))
    while edad < 0 or edad > 100:
        edad = int(input("ERROR! Indique una edad válida: "))

    entrada(edad)

if __name__ == "__main__":
    main()