#Para empezar, define una nueva función que reciba 3 parámetros. Esta función debe usar el primer parámetro para decidir qué operación hacer (suma, resta, multiplicación o división) y aplicarlo sobre los 2 parámetros restantes.

#Ejemplo: resultado = tufuncion(“multiplicar”, 5, 4). (El resultado debería ser igual a 20)
#Nota: Aquí estoy considerando que la función se llama “tufuncion”. En tu ejercicio pon el nombre que gustes a tu función.


def bienvenido():
        print("++++++++++++ Bienvenido ++++++++++++")
        print("+++++++++ Funnciones ++++++++++++++++")
        print("Ingrese su nombre:")
        nombre = input()
        print("Ingrese su apellido:")
        apellido = input()
        print("Bienvenido ", nombre , apellido)


def operacion():
        while True:
                print("Que operacion deseas Realizar")
                print("1: Multiplicar")
                print("2: Sumar")
                print("3: Restar")
                print("4: Dividir")
                print("5: Salir del programa")
                respuesta = int(input())

                if respuesta == 1:
                    print("Ingrese un numero a multiplicar:")
                    multiplicar = int(input())
                    print("Ingrese otro numero a multiplicar:")
                    multiplicar1 = int(input())
                    print("El resultado de la multiplicacion es: ", multiplicar * multiplicar1)

                elif respuesta == 2:
                        print("Ingrese un numero a sumar:")
                        sumar = int(input())
                        print("Ingrese otro numero a sumar:")
                        sumar1 = int(input())
                        print("El resultado de la suma es: ", sumar + sumar1)

                elif respuesta == 3:
                        print("Ingrese un numero a restar:")
                        restar = int(input())
                        print("Ingrese otro numero a restar:")
                        restar1 = int(input())
                        print("Su resultado es: ", restar - restar1)

                elif respuesta == 4:
                        print("Ingrese un numero a dividir:")
                        dividir = int(input())
                        print("Ingrese el numero entre cuanto quiere dividir:")
                        dividir1 = int(input())
                        print("Su resultado de la division es: ", dividir / dividir1)

                elif respuesta == 5:
                        print("Hasta Luego gracias por usar la calculadora")
                        break

bienvenido()
operacion()
