# Autor: Oscar Alejandro Torres Maya, A01377686
# Descripcion: Pregunta al usuario si quiere hacer una division y calcular su residuo o
#              le pregunta si quiere calcular el mayor de una lista de numeros

# Funcion para dividir y calcular el residuo
def dividir():
    print("")
    print("Calculando divisiones")
    dividendo = int(input("Teclea el dividendo: "))
    divisor = int(input("Teclea el divisor: "))

    primerDividendo = dividendo
    cociente = 0
    residuo = 0

    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
        residuo = dividendo

    print ("%d / %d = %d, sobra %d" %(primerDividendo, divisor, cociente, residuo))
    print("")


# Funcion para encontrar el mayor de una lista de numeros
def encontrarMayor():
    lista = 0
    contador = 0
    mayor = 0
    print("")
    print("Teclea una serie de números para encontrar el mayor.")
    while lista != -1:
        x = int(input("Teclea un número [-1 para salir]: "))
        contador = contador + 1

        if x > mayor:
            mayor = x

        elif contador == 1 and x == -1:
            print("No hay valor mayor")
            print("")
            break

        if x == -1:
            print("El mayor es:",mayor)
            print("")
            break


# Funcion principal
def main():
    opcion = 0
    while opcion != 3:
        print("""Misión 07. Ciclos while 
Autor: Oscar Alejandro Torres Maya
Matrícula: A01377686
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
        opcion = int(input("Teclea tu opción: "))
        if opcion < 1 or opcion > 3:
            print("ERROR, teclea 1, 2 o 3")
            print("")
        elif opcion == 1:
            dividir()
            print("")
        elif opcion ==2:
            encontrarMayor()
            print("")
        elif opcion == 3:
            print("")
            print("Gracias por usar este programa, regresa pronto.")
            break

# Llamar a la funcion principal
main()