import Metricas as m
from statistics import multimode

archivo = open("wine_training60.0.csv", "r")
contenido = archivo.readlines()

print('\nArchivo Completo: ')
for l in contenido:
    print(l, end="")
print("\n\n")


lista = [linea.split(",") for linea in contenido]

print("Lista de listas separadas por comas: ")
for l in lista:
    print(l)
print("\n\n")


instancia = [[list(map(float, x[:13])), x[13]] for x in lista]

print("Total de datos de la Instancia", len(instancia))

print("Instancia de entrenamiento:")
for l in instancia:
    print(l)
print("\n\n")


###########################################################################
archivo = open("wine_test60.0.csv","r")
contenido = archivo.readlines()


print('\nArchivo Completo: ')
for l in contenido:
    print(l, end="")
print("\n\n")


lista = [linea.split(",") for linea in contenido]


print("Lista de listas separadas por comas: ")
for l in lista:
    print(l)
print("\n\n")

prueba = [[list(map(float, x[:13])), x[13]] for x in lista]

print("Total de datos de la Instancia", len(prueba))

print("Instancia de prueba:")
for l in prueba:
    print(l)
print("\n\n")

##############################################################################
listaResultados = list()
for K in range(1, 11):
    print("----------------------------------------------")
    print("Resultados con K: {0}".format(K))
    contAciertos = 0

    for registroNC in prueba:
        print("Clasificación del registro: ")
        print(registroNC)

        NC = registroNC[0]

        estructuraDatos = {}

        for NoCaso, i in enumerate(instancia):
            distancia_NC_i = m.Canberra(NC, i[0])
            estructuraDatos[NoCaso] = distancia_NC_i

        ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1])

        temporalK = []
        for i in range(K):
            NoCaso = ordenado[i][0]
            registro = instancia[NoCaso]
            temporalK.append(registro[1])

        print("Clases de los vectores más cercanos al registro NC:")
        print(temporalK)
        print("\n\n")

        moda = multimode(temporalK)
        respKnn = moda[0]

        print("Clase asignada por el KNN: " + str(respKnn))
        print("Clase Real: " + registroNC[1])

        if str(respKnn) == registroNC[1]:
            contAciertos += 1

    print("Total de aciertos: " + str(contAciertos))
    print("Total de pruebas: " + str(len(prueba)))
    print("Rendimiento: " + str(contAciertos/len(prueba)*100))
    listaResultados.append([K,(contAciertos/len(prueba)*100)])
    print('\n')

print('RESULTADOS')
listaResultados = sorted(listaResultados, key=lambda x: x[1], reverse=True)
for x in listaResultados:
    print("K: " + str(x[0]) + "  Rendimiento: " + str(x[1]))

print("El valor de K recomendado es " + str(listaResultados[0][0]))
