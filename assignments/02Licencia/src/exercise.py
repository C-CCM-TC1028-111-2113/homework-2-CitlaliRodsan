
def main():
    #Escribe tu código debajo de esta línea
    
    edad = int(input("Ingresa tu edad: "))
    if edad<=0:
        print("Respuesta incorrecta")
    elif edad<18:
        print("No cumples requisitos")
    else:
        ido = str(input("¿Tienes identificación oficial? (s/n): "))
        if not(ido=='s' or ido=='n'):
                print("Respuesta incorrecta")
        elif edad>=18 and ido=='s':
                print("Trámite de licencia concedido")
        elif edad<18 or ido=='n':
                print("No cumples requisitos")


if __name__ == '__main__':
    main()
