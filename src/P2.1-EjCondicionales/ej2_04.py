"""
Buenas Diego, si estás viendo esto y ves una excepción, no te asustes, es que estoy modificando el ejercicio después de tú haber explicado las excepciones, y aquí se puede utilizar una excepción sencilla de los números enteros. Simplemente lo estoy practicando para que me quede claro. 
Saludos, máquina ;D
"""
def pedirnumero():
    numero = (input("Introduzca un núemro entero: "))
    try:
        n_entero = int(numero)
    except ValueError:
        print("Usted no ha introducido un número entero.")

    return n_entero


def main():
    numero = pedirnumero()
    if numero % 2 == 0:
        print("El número introducido es par.")
    else:
        print("El número introducido es impar.")

if __name__ == "__main__":
    main()