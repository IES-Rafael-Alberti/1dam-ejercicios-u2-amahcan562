"""
Buenas Diego, si estás viendo esto y ves una excepción, no te asustes, es que estoy modificando el ejercicio después de tú haber explicado las excepciones, y aquí se puede utilizar una excepción sencilla de los números enteros. Simplemente lo estoy practicando para que me quede claro. 
Saludos, máquina ;D
"""
def numero(n_entero):
    if n_entero % 2 == 0:
        print("El número introducido es par.")
    else:
        print("El número introducido es impar.")

def main():
    num = (input("Introduzca un núemro entero: "))
    try:
        n_entero = int(num)
        numero(n_entero)
    except ValueError:
        print("Usted no ha introducido un número entero.")
    
if __name__ == "__main__":
    main()