def main():
    # Escribe el código adecuado para completar el programa
    
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    if x>y and x>z:
        mayor=x
        if y>z:
            medio=y
            menor=z
        else:
            medio=z
            menor=y

    elif y>x and y>z:
        mayor=y
        if x>z:
            medio=x
            menor=z
        else:
            medio=z
            menor=x

    elif z>y and z>x:
        mayor=z
        if y>x:
            medio=y
            menor=x
        else:
            medio=x
            menor=y

    print(menor)
    print(medio)
    print(mayor)

if __name__=='__main__':
    main()
