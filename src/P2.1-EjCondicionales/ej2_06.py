def pedirNombre():
    nombre = input("Introduzca su nombre: ")
    return nombre

def pedirSexo():
    sexo = input("Introduzca su sexo (M o F): ")
    while sexo != "M" or sexo != "F":
        sexo = input("ERROR! Introduzca su sexo (M o F): ")
    return sexo

def grupo_pertenece(nombre, sexo):
    if (sexo == "F" and nombre < "M") or (sexo == "M" and nombre > "N"):
        grupo = "A"
    else:
        grupo = "B"
    return grupo

def main():
    nombre = pedirNombre()
    sexo = pedirSexo()
    grupo = grupo_pertenece(nombre, sexo)
    print(f"Te corresponde el grupo {grupo}.")
    
if __name__ == "__main__":
    main()