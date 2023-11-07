def pedirNombre():
    nombre = input("Introduzca su nombre: ")
    nombre = nombre.upper()
    return nombre

def pedirSexo():
    sexo = input("Introduzca su sexo (M o F): ")
    sexo = sexo.upper()
    while sexo != "M" and sexo != "F":
        sexo = input("ERROR! Introduzca su sexo (M o F): ")
        sexo = sexo.upper()

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