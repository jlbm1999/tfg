import qsimov as qj
import circuitos as ct
import random as rnd

# Para almacenar todos los grafos que se vayan a probar

prueba = [[0,1,1,0],[0,0,1],[0,1],[0]]
docMatrix = [[0,1,1,1,0],[0,0,0,1],[0,0,1],[0,1],[0]]
M2 = []

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
            result.append(str(i) + ': ' + str((values[i] * 100).round(1)))
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

def randomMatrixGenerator(nNodes):
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
    return cutHalfMatrix(m)

# Recibe una matriz y devuelve la parte superior
def cutHalfMatrix(matrix):
    count = 0
    for i in range(len(matrix)):
        matrix[i] = matrix[i][count:]
        count += 1
    return matrix