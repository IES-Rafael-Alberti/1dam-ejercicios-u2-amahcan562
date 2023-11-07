def tramos():
    renta_anual = float(input("Introduzca su renta anual: "))
    if renta_anual < 10000:
        renta_anual = "5%"
    elif renta_anual >= 10000 and renta_anual <20000:
        renta_anual = "15%"
    elif renta_anual >= 20000 and renta_anual <35000:
        renta_anual = "20%"
    elif renta_anual >= 35000 and renta_anual <60000:
        renta_anual = "30%"
    elif renta_anual >= 60000:
        renta_anual = "45%"
    
    return renta_anual

def main():
    valor = tramos()
    print(f"Le corresponde un valor del {valor}.")

if __name__ == "__main__":
    main()