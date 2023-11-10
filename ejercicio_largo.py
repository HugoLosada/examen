#Creamos un programa que analice la temperatura de varias semanas 
#Establecemos los datos principales:
temperatura = [
    [22,24,19,21,25,23,20],  #Semana 1
    [20,22,21,23,24,22,21],  #Semana 2
    [23,21,20,22,24,25,23]   #Semana 3
]
# Creamos una lista para representar el promedio histórico de temperaturas para cada semana
temperatura_promedio_historica = [
    [21, 23, 18, 20, 24, 22, 19],  # Promedio histórico para Semana 1
    [19, 21, 20, 22, 23, 21, 20],  # Promedio histórico para Semana 2
    [22, 20, 19, 21, 23, 24, 22]   # Promedio histórico para Semana 3
   ]          


#Creamos una función para cada uno de los cálculos que nos piden
#Funcion para calcular el promedio semanal:
#Utiizamos el for i in range para iterar sobre cada semana en la lista de temperatura y accdemos a la semana con el índice i.
def calcular_promedio_semana(temperaturas):
    for i in range(len(temperaturas)):
        semana = temperaturas[i]
        promedio = sum(semana) / len(semana)
        print(f"El promedio de temperatura para la Semana {i + 1}: {promedio: } °C")
#Función para calcular el dia más caluroso:
def encontrar_dia_mas_caluroso(temperaturas):
    for i in range(len(temperaturas)):
        semana = temperaturas[i]
        dia_caluroso = semana.index(max(semana)) + 1
        print(f"El dia más caluroso en la Semana {i + 1}: Día {dia_caluroso}")
#Función para calcular las semanas que tienen una temperatura moderada 
def semanas_temperatura_moderada(temperaturas):
    for i in range(len(temperaturas)):
        semana = temperaturas[i]
        temperaturas_moderadas = all(20 <= temp <= 25 for temp in semana)
        if temperaturas_moderadas:
            print(f"Semana {i + 1}: Todas las temperaturas entre 20 y 25 grados.")
#Función para calcular las fluctuaciones: 
def fluctuaciones_temperatura_semanal(temperaturas):
    for i in range(len(temperaturas)):
        semana = temperaturas[i]
        # Calculamos las fluctuaciones de temperatura para cada día de la semana
        # La expresión [semana[j] - semana[j-1] if j > 0 else 0 for j in range(len(semana))]
        # crea una lista de diferencias entre temperaturas consecutivas en la semana.
        # Si j es 0 (primer día), la fluctuación es 0, de lo contrario, calcula la diferencia.
        fluctuaciones = [semana[j] - semana[j-1] if j > 0 else 0 for j in range(len(semana))]
        print(f"Fluctuaciones de temperatura en la Semana {i + 1}: {fluctuaciones}")

# Función para comparar temperaturas promedio actuales y históricas
def comparar_temperaturas_promedio(temperaturas_actuales, temperaturas_historicas):
    for i in range(len(temperaturas_actuales)):
        promedio_actual = sum(temperaturas_actuales[i]) / len(temperaturas_actuales[i])
        promedio_historico = sum(temperaturas_historicas[i]) / len(temperaturas_historicas[i])
        diferencia = promedio_actual - promedio_historico
        print(f"Diferencia de temperatura promedio para la Semana {i + 1}: {diferencia:} °C")


#Llamamos a cada función y le damos como argumento la lista de la temperatura

calcular_promedio_semana(temperatura)
encontrar_dia_mas_caluroso(temperatura)
semanas_temperatura_moderada(temperatura)
fluctuaciones_temperatura_semanal(temperatura)
comparar_temperaturas_promedio(temperatura, temperatura_promedio_historica)


