def main():
    #escribe tu código abajo de esta línea
    
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    mayor = num1
    if num2>num1 and num2>num3:
        mayor = num2
    elif num3>num1 and num3>num2:
        mayor = num3
        
    print(mayor)

if __name__=='__main__':
    main()
