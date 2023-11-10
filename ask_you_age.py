#Creamos un programa que le pida al usuario la edad y si es mayor de edad le deje pasa
#Creamos una función y la llamamos mayor_de_edad

def mayor_de_edad():
    #Utilizamos el try y except para el manejo de errores, por si el usuario nos da un valor que no es un int
    try:

    #Creamos la variable edad y utilizamos el int porque el número que nos va a dar el usuario va a ser un entero
    #Y el input para que el usuario pueda escribirnos la edad.
        edad = int(input("Dime tu edad: "))
    #Utilizamos el if para crear la condición, si el usuario nos da un valor mayor o igual a 18 podrá pasar.
        if edad >= 18:
                print("Eres mayor de edad puedes pasar")
        else:
        #Si el usuario nos da un valor que no sea igual o mayor que 0, entonces le aparecerá el siguiente mensaje.
            print("Lo siento eres menor de edad no te puedo dejar pasar.")
    except ValueError:
         #Si el usuario nos da una respuesta que no sea un número entero le aparecerá el siguiente mensaje.
         print("Por favor, tienes que ingresaar un número entero.")
#Llamamos a la función
mayor_de_edad()
