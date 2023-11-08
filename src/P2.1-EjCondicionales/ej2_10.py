def ingredientes(opcion):
    if opcion == "si":
        eleccion = input("Todas las pizzas llevan tomate y mozzarella. Además, puede añadir pimiento o tofu. ¡Escoja uno!: ")
        tipo = "vegetariana"
        eleccion = eleccion.lower()
        while eleccion != "pimiento" and eleccion != "tofu":
            eleccion = input("ERROR! Elija un ingrediente: ")
    else:
        eleccion = input("Todas las pizzas llevan tomate y mozzarella. Además, puede añadir pepperoni, jamón o salmón. ¡Escoja uno!: ")
        tipo = "normal"
        eleccion = eleccion.lower()
        while eleccion != "pepperoni" and eleccion != "jamón" and eleccion != "jamon" and eleccion != "salmón" and eleccion != "salmon":
            eleccion = input("ERROR! Elija un ingrediente: ")

    return eleccion, tipo

def main():
    opcion = input("¿Quiere usted una pizza vegetariana? (SI/NO) ")
    opcion = opcion.lower()
    while opcion != "si" and opcion != "no":
        opcion = input("ERROR! Responda con SI o NO:  ")
    
    eleccion, tipo = ingredientes(opcion)

    print(f"La pizza escogida es {tipo} y lleva tomate, mozzarella y {eleccion}.")


if __name__ == "__main__":
    main()