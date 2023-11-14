def pedirContraseña():
    contraseñaIntroducida = input("Introduzca una contraseña: ")
    return contraseñaIntroducida.lower()

def main():
    contraseñaAlmacenada = ("contraseña")

    contraseñaIntroducida = pedirContraseña()
    if contraseñaIntroducida == contraseñaAlmacenada:
        print("Contraseña correcta.")
    else:
        print("Contraseña incorrecta.")

if __name__ == "__main__":
    main()