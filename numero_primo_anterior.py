print("\n-----------------------------------")
print("---------- NÚMEROS PRIMOS ---------")
print("-----------------------------------")
print("\n1.Numeros primos de 1 a 200\n2.Numeros primos anteriores a cierto número\n3.Saber si un número es primo o no")
opcion = int(input("Eliga una opcion: "))
if opcion == 1:
    numero = 1
    contador = 0
    while numero <= 200:
        contador = 1
        x = 0
        while contador <= numero:
            if numero % contador == 0:
                x += 1    
            contador += 1
        if x == 2:
            print(numero)
        numero += 1

if opcion == 2:
    numero = 1
    contador = 0
    PedirNumero = int(input("Ingrese su número: "))
    while numero <= PedirNumero:
        contador = 1
        x = 0
        while contador <= numero:
            if numero % contador == 0:
                x += 1    
            contador += 1
        if x == 2:
            print(numero)
        numero += 1

if opcion == 3:
    PedirNumero = int(input("Ingrese su número: "))
    contador = 2
    bandera = False
    if PedirNumero > 1:
        while contador < PedirNumero:
            if (PedirNumero % contador) == 0:
                bandera = True
            contador += 1
    else:
        print(str(PedirNumero), " no es un número primo")
    if bandera == True:
        print(str(PedirNumero), " no es un número primo")
    else:
        print(str(PedirNumero), " es un número primo")
