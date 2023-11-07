def pedirpalabra():
    palabra = input("Introduzca una palabra: ")
    while len(palabra) == 0:
        palabra = input("ERROR! Introduzca una palabra: ")
    return palabra

def main():
    print((pedirpalabra() + "\n") * 10)

if __name__ == "__main__":
    main()