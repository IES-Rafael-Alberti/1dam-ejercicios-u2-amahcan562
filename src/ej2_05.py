def tributar(edad, ingresos):
    if ingresos < 1000 or edad < 16:
        print("Usted no tributa.")
    else:
        print("Usted sí tributa.")

def main():
    edad = int(input("Introduzca su edad: "))
    ingresos = float(input("Introduzca sus ingresos: "))
    tributar(edad, ingresos)
if __name__ == "__main__":
    main()