def rendimiento(puntuacion, sueldo_base):
    
    if puntuacion >= 0.0 and puntuacion < 0.4:
        nivel = "inaceptable"
        sueldo = sueldo_base
    elif puntuacion >= 0.4 and puntuacion < 0.6:
        nivel = "aceptable"
        sueldo = sueldo_base + (sueldo_base * 0.4)
    elif puntuacion >= 0.6:
        nivel = "meritorio"
        sueldo = sueldo_base + (sueldo_base * 0.6)

    return nivel, sueldo

def main():
    sueldo_base = 2400

    puntuacion = float(input("Introduzca su puntuación final: "))
    while puntuacion < 0 or puntuacion > 1:
        puntuacion = float(input("ERROR! Introduzca una puntuación válida: "))
    
    tupla = rendimiento(puntuacion, sueldo_base)
    print(f"Su nivel es {tupla[0]} y el sueldo que recibirá es de {tupla[1]}€.")

if __name__ == "__main__":
    main()