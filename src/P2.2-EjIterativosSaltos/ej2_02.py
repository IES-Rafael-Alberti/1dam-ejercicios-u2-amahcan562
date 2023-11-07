def pediredad():
    edad = int(input("Introduzca su edad: "))
    while edad < 1 or edad > 100:
        edad = int(input("ERROR! Introduzca una edad válida: "))
    
    return edad

def main():
    edad = pediredad()
    n = 1
    while n <= edad:
        print(n, end=" ")
        n += 1

if __name__ == "__main__":
    main()