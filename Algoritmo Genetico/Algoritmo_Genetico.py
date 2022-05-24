import math
import random as rnd


#Bohachevsky
def calc_FO2(indv):
    cont = 0
    for i in range(len(indv)-1):
        cont += ((indv[i]**2) + (2*(indv[i+1]**2)) - (0.3 * math.cos(3 * math.pi * indv[i])) -
                 (0.4 * math.cos(4 * math.pi * indv[i+1])) + 0.7)
    return cont

#Sphere
def calc_FO1(indv):

    cont = 0
    for i in indv:
        cont += i**2
    return cont

#Cigar
def calc_FO(indv):
    x0 = (indv[0]) ** 2
    sumatoria = 0
    for i in range(1,len(indv)):
        sumatoria += (indv[i]) ** 2

    return x0 + pow(10,6) * sumatoria


tot_genes = 1000


tot_individuos = 120


poblacion = []
for i in range(tot_individuos):


    vector = [ float(rnd.randrange(-10,10)) for i in range(tot_genes)]
    print(vector)
    ##               vector , FO
    poblacion.append([vector, calc_FO1(vector)])

#print("Poblacion Inicial: ")
#for indv in poblacion:
#    print(indv)

it = 1
mejorActual = 99999999
while it<=1000:
    print("Iteracion : ", it)
    it+=1

    padres = []
    tot_padres = 20


    #    Reverse es false, porque fO = 0 siendo que los mejores son los que se acerquen a 0
    poblacion.sort(key= lambda x:x[1], reverse=False)


    #    Para sphere es mejor los menores
    if poblacion[0][1] <= mejorActual:
        mejorActual = poblacion[0][1]



    poblacion = poblacion[0:tot_individuos-tot_padres]

    for i in range(tot_padres):
        indexPadre1 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
        indexPadre2 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
        while(indexPadre1==indexPadre2):
            indexPadre2 = rnd.randint(0, tot_padres - 1)  # aleatorio entre 0 y n-1

        tempPadre1 = poblacion[indexPadre1]
        tempPadre2 = poblacion[indexPadre2]


        if tempPadre1[1] >= tempPadre2[1]:
            padres.append(tempPadre1[0].copy())
        else:
            padres.append(tempPadre2[0].copy())



    hijos = []
    for i in range(0,tot_padres, 2):
        tempPadre1 = padres[i]
        tempPadre2 = padres[i+1]

        #Generar un aleatorio
        puntoCruza = rnd.randint(0, tot_genes-1)


        puntoCruza += 1  # +1 -> puntoCruza incluyente
        hijo1 = tempPadre1[:puntoCruza] + tempPadre2[puntoCruza:]
        hijo2 = tempPadre2[:puntoCruza] + tempPadre1[puntoCruza:]

        hijos.append([hijo1, 0])
        hijos.append([hijo2, 0])


    #Mutacion
    probMuta = 0.9
    for indexHijo in range(len(hijos)):
        hijo = hijos[indexHijo][0]

        for indexGen in range(len(hijo)):
            r = rnd.random() # 0 - 1
            if r >= probMuta:

                rnd.uniform(0,0.4)
                val = 0.1 if rnd.random() >= 0.5 else  0.9
                val *= hijo[indexGen]

                hijo[indexGen] = val

        hijos[indexHijo][1] = calc_FO1(hijo)

    poblacion += hijos

    print("Mejor Solucion Actual:" , mejorActual)