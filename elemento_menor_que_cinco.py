#Creamos una lista con varios números

lista = [1,2,3,4,5,6,7,8,9,10]

#Cremos un función donde le damos la lista como argumento y le decimos que recorra cada elemento de la lista y que si es menor de 5 lo pinte.

def elementos_menores_de_cinco(lista):
    for num in lista:
        if num < 5:
            print(num)


elementos_menores_de_cinco(lista)