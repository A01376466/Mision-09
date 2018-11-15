# Autor: Ivan
# Descripción: Diferentes funciones que utilizan listas para realizar tareas.


# Esta función regresa una lista con solo los números pares de la lista orginal.
def extraerPares(listaPrueba1):
    listaPares = []
    if len(listaPrueba1) > 0:
        for x in range(len(listaPrueba1)):
            if listaPrueba1[x] % 2 == 0:
                listaPares.append(listaPrueba1[x])

    return listaPares


# Esta función crea una lista con los números mayores al anterior en la lista original.
def extraerMayoresPrevio(listaPrueba1):
    listaMayoresPrevio = []
    if len(listaPrueba1) > 0:
        for x in range(1, len(listaPrueba1)):
            if listaPrueba1[x] > listaPrueba1[x - 1]:
                listaMayoresPrevio.append(listaPrueba1[x])

    return listaMayoresPrevio


# Esta función intercambia de lugar las parejas de números y los regresa en una nueva lista.
def intercambiarParejas(listaPrueba1):
    listaParejasIntercambiadas = []
    if len(listaPrueba1) > 0:
        for x in range(1, len(listaPrueba1), 2):
            listaParejasIntercambiadas.append(listaPrueba1[x])
            listaParejasIntercambiadas.append(listaPrueba1[x - 1])
    if len(listaPrueba1) % 2 != 0:
        listaParejasIntercambiadas.append(listaPrueba1[len(listaPrueba1) - 1])

    return listaParejasIntercambiadas


# Esta función intercambia los lugares del mayor y menor valor de una lista, los cambios son directamente
# en la lista original.
def intercambiarMM(listaCambiantePrueba1):
    if len(listaCambiantePrueba1) > 0:
        valorMayor = listaCambiantePrueba1[0]
        valorMenor = listaCambiantePrueba1[0]
        for x in range(1, len(listaCambiantePrueba1)):
            if listaCambiantePrueba1[x] > valorMayor:
                valorMayor = listaCambiantePrueba1[x]
            if listaCambiantePrueba1[x] < valorMenor:
                valorMenor = listaCambiantePrueba1[x]
        indiceMayor = listaCambiantePrueba1.index(valorMayor)
        indiceMenor = listaCambiantePrueba1.index(valorMenor)
        listaCambiantePrueba1[indiceMayor] = valorMenor
        listaCambiantePrueba1[indiceMenor] = valorMayor

    return listaCambiantePrueba1


# Esta función realiza un promedio de los valores de una lista sin el valor más alto y sin el valor más bajo.
def promediarCentro(listaPrueba1):
    promedioCentro = 0
    if len(listaPrueba1) > 2:
        listaPromedioCentro = listaPrueba1.copy()
        valorMayor = listaPromedioCentro[0]
        valorMenor = listaPromedioCentro[0]
        for x in range(1, len(listaPromedioCentro)):
            if listaPromedioCentro[x] > valorMayor:
                valorMayor = listaPromedioCentro[x]
            if listaPromedioCentro[x] < valorMenor:
                valorMenor = listaPromedioCentro[x]
        listaPromedioCentro.remove(valorMayor)
        listaPromedioCentro.remove(valorMenor)
        for x in range(len(listaPromedioCentro)):
            promedioCentro += listaPromedioCentro[x]
        promedioCentro = int(promedioCentro / len(listaPromedioCentro))

    return promedioCentro


# Esta función calcula el promedio y la desviación estándar de los valores de una lista.
def calcularEstadistica(listaPrueba1):
    promedio = 0
    desviacion = 0
    if len(listaPrueba1) > 0:
        for x in range(len(listaPrueba1)):
            promedio += listaPrueba1[x]
        promedio = promedio / len(listaPrueba1)
        for y in range(len(listaPrueba1)):
            desviacion += (listaPrueba1[y] - promedio) ** 2
        desviacion = (desviacion / (len(listaPrueba1) - 1)) ** (1 / 2)
    estadistica = promedio, desviacion

    return estadistica


# Esta función suma los valores de una lista sin contar los números 13 o los números a lado de estos.
def calcularSuma(listaPrueba1):
    sumaSinTrece = 0
    if len(listaPrueba1) > 0:
        if listaPrueba1[0] != 13:
            sumaSinTrece += listaPrueba1[0]
        if listaPrueba1[len(listaPrueba1) - 1] != 13:
            sumaSinTrece += listaPrueba1[len(listaPrueba1) - 1]
        for x in range(1, len(listaPrueba1) - 1):
            if listaPrueba1[x] != 13 and listaPrueba1[x - 1] != 13 and listaPrueba1[x + 1] != 13:
                sumaSinTrece += listaPrueba1[x]

    return sumaSinTrece


# Esta es la función principal que establece las listas y manda a llamar a todas las funciones.
def main():
    listaPrueba1 = [1, 2, 3, 4, 5, 87, 13, 5, 32, 21, 95, 35, 42, 2, 3, 4]
    listaPrueba2 = []
    listaPrueba3 = [5, 7, 3]
    listaPrueba4 = [6, 5, 4, 3, 2, 1]
    listaPrueba5 = [2, 8, 9, 17, 13, 8, 5, 3, 1]

    listaCambiantePrueba1 = [1, 2, 3, 4, 5, 87, 32, 21, 95, 35, 42, 2, 3, 4]
    listaCambiantePrueba2 = []
    listaCambiantePrueba3 = [5, 7, 3]
    listaCambiantePrueba4 = [6, 5, 4, 3, 2, 1]
    listaCambiantePrueba5 = [2, 8, 9, 17, 5, 3, 1]

    pares1 = extraerPares(listaPrueba1)
    pares2 = extraerPares(listaPrueba2)
    pares3 = extraerPares(listaPrueba3)
    pares4 = extraerPares(listaPrueba4)
    pares5 = extraerPares(listaPrueba5)
    print("Problema 1: Regresa una lista con los valores pares de la lista original.")
    print("Con la lista", listaPrueba1, ", regresa", pares1)
    print("Con la lista", listaPrueba2, ", regresa", pares2)
    print("Con la lista", listaPrueba3, ", regresa", pares3)
    print("Con la lista", listaPrueba4, ", regresa", pares4)
    print("Con la lista", listaPrueba5, ", regresa", pares5)
    print("")

    mayorPrevio1 = extraerMayoresPrevio(listaPrueba1)
    mayorPrevio2 = extraerMayoresPrevio(listaPrueba2)
    mayorPrevio3 = extraerMayoresPrevio(listaPrueba3)
    mayorPrevio4 = extraerMayoresPrevio(listaPrueba4)
    mayorPrevio5 = extraerMayoresPrevio(listaPrueba5)
    print("Problema 2: Regresa una lista con los valores mayores al anterior en la lista original.")
    print("Con la lista", listaPrueba1, ", regresa", mayorPrevio1)
    print("Con la lista", listaPrueba2, ", regresa", mayorPrevio2)
    print("Con la lista", listaPrueba3, ", regresa", mayorPrevio3)
    print("Con la lista", listaPrueba4, ", regresa", mayorPrevio4)
    print("Con la lista", listaPrueba5, ", regresa", mayorPrevio5)
    print("")

    parejasIntercambiadas1 = intercambiarParejas(listaPrueba1)
    parejasIntercambiadas2 = intercambiarParejas(listaPrueba2)
    parejasIntercambiadas3 = intercambiarParejas(listaPrueba3)
    parejasIntercambiadas4 = intercambiarParejas(listaPrueba4)
    parejasIntercambiadas5 = intercambiarParejas(listaPrueba5)
    print("Problema 3: Regresa lista con parejas de valores intercambiados del lugar de la lista original.")
    print("Con la lista", listaPrueba1, ", regresa", parejasIntercambiadas1)
    print("Con la lista", listaPrueba2, ", regresa", parejasIntercambiadas2)
    print("Con la lista", listaPrueba3, ", regresa", parejasIntercambiadas3)
    print("Con la lista", listaPrueba4, ", regresa", parejasIntercambiadas4)
    print("Con la lista", listaPrueba5, ", regresa", parejasIntercambiadas5)
    print("")

    print("Problema 4: Regresa la lista original con el valor mayor y menor intercambiados de lugar.")
    print("Con la lista", listaPrueba1, ", regresa", intercambiarMM(listaCambiantePrueba1))
    print("Con la lista", listaPrueba2, ", regresa", intercambiarMM(listaCambiantePrueba2))
    print("Con la lista", listaPrueba3, ", regresa", intercambiarMM(listaCambiantePrueba3))
    print("Con la lista", listaPrueba4, ", regresa", intercambiarMM(listaCambiantePrueba4))
    print("Con la lista", listaPrueba5, ", regresa", intercambiarMM(listaCambiantePrueba5))
    print("")

    promedioCentro1 = promediarCentro(listaPrueba1)
    promedioCentro2 = promediarCentro(listaPrueba2)
    promedioCentro3 = promediarCentro(listaPrueba3)
    promedioCentro4 = promediarCentro(listaPrueba4)
    promedioCentro5 = promediarCentro(listaPrueba5)
    print("Problema 5: Regresa el promedio centro de una lista.")
    print("Con la lista", listaPrueba1, ", regresa", promedioCentro1)
    print("Con la lista", listaPrueba2, ", regresa", promedioCentro2)
    print("Con la lista", listaPrueba3, ", regresa", promedioCentro3)
    print("Con la lista", listaPrueba4, ", regresa", promedioCentro4)
    print("Con la lista", listaPrueba5, ", regresa", promedioCentro5)
    print("")

    mediaDesviacion1 = calcularEstadistica(listaPrueba1)
    mediaDesviacion2 = calcularEstadistica(listaPrueba2)
    mediaDesviacion3 = calcularEstadistica(listaPrueba3)
    mediaDesviacion4 = calcularEstadistica(listaPrueba4)
    mediaDesviacion5 = calcularEstadistica(listaPrueba5)
    print("Problema 6: Regresa la media y la desviación estándar de una lista.")
    print("Con la lista", listaPrueba1, ", regresa", mediaDesviacion1)
    print("Con la lista", listaPrueba2, ", regresa", mediaDesviacion2)
    print("Con la lista", listaPrueba3, ", regresa", mediaDesviacion3)
    print("Con la lista", listaPrueba4, ", regresa", mediaDesviacion4)
    print("Con la lista", listaPrueba5, ", regresa", mediaDesviacion5)
    print("")

    sumaSinTrece1 = calcularSuma(listaPrueba1)
    sumaSinTrece2 = calcularSuma(listaPrueba2)
    sumaSinTrece3 = calcularSuma(listaPrueba3)
    sumaSinTrece4 = calcularSuma(listaPrueba4)
    sumaSinTrece5 = calcularSuma(listaPrueba5)
    print("Problema 7: Regresa la suma de los números de una lista que no son trece o que no van pegados al trece.")
    print("Con la lista", listaPrueba1, ", regresa", sumaSinTrece1)
    print("Con la lista", listaPrueba2, ", regresa", sumaSinTrece2)
    print("Con la lista", listaPrueba3, ", regresa", sumaSinTrece3)
    print("Con la lista", listaPrueba4, ", regresa", sumaSinTrece4)
    print("Con la lista", listaPrueba5, ", regresa", sumaSinTrece5)
    print("")


main()
