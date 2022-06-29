from math import perm
import qsimov as qj
import circuitos as ct
import random as rnd
import itertools
import numpy as np

# Para almacenar todos los grafos que se vayan a probar

prueba = [[0,1,1,0],[0,0,1],[0,1],[0]]
prueba2 = [ [0,1,1,0],
            [1,0,0,1],
            [1,0,0,1],
            [0,1,1,0]]
docMatrix = [[0,1,1,1,0],[0,0,0,1],[0,0,1],[0,1],[0]]
M1 =   [[0,0,0,0,0,1,1,0,0,1], 
        [0,0,1,1,0,0,0,0,0,1], 
        [0,1,0,1,1,0,1,1,1,1], 
        [0,1,1,0,1,1,1,1,0,0], 
        [0,0,1,1,0,1,0,0,0,1], 
        [1,0,0,1,1,0,1,0,1,1], 
        [1,0,1,1,0,1,0,1,1,1], 
        [0,0,1,1,0,0,1,0,1,1], 
        [0,0,1,0,0,1,1,1,0,0], 
        [1,1,1,0,1,1,1,1,0,0]]

petersen = [[0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0], 
            [0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0], 
            [0 , 1 , 0 , 0, 0 , 1 , 0 , 0], 
            [0 , 1, 0 , 0 , 0 , 1 , 0], 
            [0 , 0 , 0 , 0 , 0 , 1], 
            [0 , 0 , 1 , 1 , 0], 
            [0 , 0 , 1 , 1], 
            [0 , 0 , 1], 
            [0, 0], 
            [0]]
pentagonal =    [[0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0], 
                [0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0], 
                [0 , 1 , 0 , 0 , 0 , 1 , 0 , 0], 
                [0 , 1 , 0 , 0 , 0 , 1 , 0], 
                [0 , 0 , 0 , 0 , 0 , 1], 
                [0 , 1 , 0 , 0 , 1], 
                [0 , 1 , 0 , 0], 
                [0 , 1 , 0], 
                [0, 1], 
                [0]]

M_3 = [[0, 0, 1], [0, 1], [0]]
M_4 = [[0, 1, 1, 1], [0, 0, 0], [0, 1], [0]]
M_5 = [[0, 0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 1], [0, 1], [0]]
M_6 = [[0, 0, 1, 1, 0, 1], [0, 1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1], [0, 1], [0]]
M_7 = [[0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1], [0, 1], [0]]
M_8 = [[0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0], [0, 1], [0]]
M_9 = [[0, 0, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1], [0, 0], [0]]
M_10 = [[0, 0, 0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1], [0, 1], [0]]
M_11 = [[0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0], [0, 1], [0]]
M_12 = [[0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1], [0, 1, 0], [0, 1], [0]]
M_13 = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0], [0, 1, 0], [0, 1], [0]]
M_14 = [[0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1], [0, 1], [0]]
M_15 = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0], [0, 0], [0]]

all_grahps = [M_3, M_4, M_5, M_6, M_7, M_8, M_9, M_10, M_11, M_12]  #, M_13, M_14, M_15
# Funcion que recibe un tiempo en segundos y lo formatea
def timeConversion(tiempo):
    horas = int(tiempo / 60 / 60)
    tiempo -= horas * 60 * 60
    minutos = int(tiempo / 60)
    tiempo -= minutos * 60
    if (horas > 1):
        return str(horas) + ' hora(s), ' + str(minutos) + ' minuto(s) ' + str(tiempo) + ' segundos'
    elif (minutos > 1):
        return str(minutos) + ' minuto(s) ' + str(tiempo) + ' segundos'
    else:
        return str(tiempo) + ' segundos'

# Obtiene los resultados de la medicion como simulador y formatea el resultado
def returnValues(values):
    result = []
    for i in range(len(values)):
        if (values[i] > 10**(-25)):
            result.append(str(i) + ': ' + str((values[i] * 100).round(2)))
        else:
            result.append(str(i) + ': 0')
    return result

# Recibe un grafo y aplica el algoritmo n veces. Luego hace la media de los porcentajes
def iteratePhaseAlgorithm(graph, rotation, iterations, nGraphs):
    output = []
    executer = qj.Drewom(extra={'return_struct':False})

    for _ in range(nGraphs):
        algoritmoFase = ct.phaseAlgorithm(graph, rotation)
        circuito = executer.execute(algoritmoFase, iterations)
        output.append(frequency(circuito, iterations))

    return output

# Devuelve el porcentaje correspondiente a cada valor
def frequency(circuit, iterations):
    invertedList = []
    for i in circuit:  # Invierte los valores de la lista y los pasa a binario
        aux = ''
        for j in i:
            if (j == True):
                aux = aux + f'{1}'
            else:
                aux = aux + f'{0}'
        invertedList.append(int(aux,2))

    result = {}
    maximo = max(invertedList)    # Obtiene la frecuencia por elemento
    for i in range(maximo + 1):
        result[i] = 0
        for j in invertedList:
            if (i == j):
                result[i] = result[i] + 1

    for i in range(len(result)):     # Pasa la frecuencia a porcentaje
        result[i] = result[i]/iterations * 100 
    return result

    # Coge la matriz a la que se le ha eliminado el nodo y se eliminan los valores
def updateMatrix(matrix, index):
    matrix.pop(index)
        
    for i in range(index):
        for j in range(len(matrix[i])):
            if (j == index):
                matrix[i].pop(j)
    return matrix

def randomMatrixGenerator(nNodes, cut=False):
    # Se genera la matriz de 0
    m = []
    for i in range(nNodes):
        m.append([])
        for _ in range(nNodes):
            m[i].append(0)
    
    # Se añaden 1 aleatorios menos en la diagonal principal
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (i is not j):
                if(rnd.random() >= 0.5):
                    m[i][j] = 1
    if cut:
        return m
    else:
        # Se devuelve la mitad de la matriz para que sea simetrica
        return cutHalfMatrix(m)

# Recibe una matriz y devuelve la parte superior
def cutHalfMatrix(matrix):
    count = 0
    for i in range(len(matrix)):
        matrix[i] = matrix[i][count:]
        count += 1
    return matrix

# Devuelve todas las posibles combinaciones de matrices de adyacencia dado un número de nodos
def getAllCombinations(nodes):
    return  [list(i) for i in itertools.product([0, 1], repeat=int((nodes*nodes - nodes)/2))]

# Construye todas las matrices de adyacencia dado un numero de nodos
def getAllMatrices(nodes):
    lst = getAllCombinations(nodes)
    # m = randomMatrixGenerator(nodes, True)
    matrices = []
    for i in lst:
        aux = randomMatrixGenerator(nodes, True)
        for j in range(len(aux)):
            for k in range(len(aux[j])):
                if ((k != 0)):
                    aux[j][k] = i.pop(0)
        matrices.append(aux)
        aux = []
    return matrices

def getPermutationMatrix(nodes):
    # Se genera la matriz de 0
    m = []
    for i in range(nodes):
        m.append([])
        for _ in range(nodes):
            m[i].append(0)

    for i in range(len(m)):
        if ((i+1) == nodes):
            m[i][0] = 1
        else:
            m[i][i+1] = 1
            
    return m

def getTransposeOfMatrix(matrix):
    transpose = []
    for i in range(len(matrix)):
        transpose.append([])
        for j in range(len(matrix[i])):
            transpose[i].append(matrix[j][i])
    return transpose

def multiplyMatrices(m1, m2):
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m2[0])):
            result[i].append(0)
            for k in range(len(m1[0])):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def permuteMatrix(matrix):
    permutation = getPermutationMatrix(len(matrix))
    transpose = getTransposeOfMatrix(permutation)
    p1 = multiplyMatrices(matrix, permutation)
    p2 = multiplyMatrices(p1, transpose)

    return p2

