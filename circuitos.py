from types import MemberDescriptorType
import qsimov as qj
import numpy as np
from qsimov import QGate
import grafos as gf


def get_QFT(num_qubits):
    QFT = QGate(num_qubits, 0, f"QFT{num_qubits}")
    for i in range(num_qubits//2):
        QFT.add_operation("SWAP", targets=[i, num_qubits-i-1])
    for i in range(num_qubits):
        QFT.add_operation("H", targets=[i])
        for j in range(num_qubits - i - 1):
            QFT.add_operation(f"RUnity({j+2})", targets=[i], controls={j+i+1})
    return QFT

def get_swapped_QFT(num_qubits):
    QFT = QGate(num_qubits, 0, f"QFT{num_qubits}")
    for i in range(num_qubits):
        QFT.add_operation("H", targets=[i])
        for j in range(num_qubits - i - 1):
            QFT.add_operation(f"RUnity({j+2})", targets=[i], controls={j+i+1})
    return QFT

# Recibe un grafo, construye un circuito y devuelve los valores de la frecuencia
def phaseAlgorithm(matrix, puerta):
    # Creamos el Oráculo
    cBasico = getCircuit(matrix, puerta)    
    nQubits = len(matrix) + len(format(len(matrix), "b"))
    nBits = len(format(len(matrix), "b"))
    targets = [i for i in range(len(matrix))]
    controls = [i + len(matrix) for i in range(len(format(len(matrix), "b")))]

    # Creamos el circuito donde aplicar el algoritmo
    c = qj.QCircuit(nQubits, nBits, 'c2')  

    # Aplicamos Hadamard a todos los qubits
    for i in range(nQubits):                    
        c.add_operation('H', i)

    nControls = len(controls)
    indexControl = 0
    while (nControls != 0):     
        for i in range(2**indexControl):       
            # Aplicamos las puertas controladas M
            c.add_operation(cBasico, targets=targets, controls=controls[indexControl])  
        indexControl += 1
        nControls -= 1
    fourier = get_swapped_QFT(nBits)   
    # Aplicamos Fourier                             
    c.add_operation(fourier.invert(), targets=controls)    
    # Medimos         
    c.add_operation('measure', targets=controls, outputs=[0,1,2])   

    return c    # Devolvemos el circuito

# Construye un circuito a partir de una matriz (no aplica Hadamard al principio)
def getCircuit(matrix, puerta):
    targets = []
    for i in range(len(matrix)):
        targets.append((i,[]))
        for j in range(len(matrix[i])):
            if (matrix[i][j] > 0):
                targets[i][1].append(j+i)

    c = qj.QGate(len(matrix), 0, 'c1')
    for i in targets:
        while(len(i[1]) > 0):
            c.add_operation(puerta, targets=i[0], controls=i[1].pop(0))

    return c

# Devuelve el porcentaje correspondiente a cada valor
def frequency(circuit, iterations):
    result = []
    for i in circuit:  # Invierte los valores de la lista y los pasa a binario
        aux = ''
        for j in i:
            if (j == True):
                aux = aux + f'{1}'
            else:
                aux = aux + f'{0}'
        result.append(int(aux,2))

    resultado = {}
    maximo = max(result)    # Obtiene la frecuencia por elemento
    for i in range(maximo + 1):
        resultado[i] = 0
        for j in result:
            if (i == j):
                resultado[i] = resultado[i] + 1

    for i in range(len(resultado)):     # Pasa la frecuencia a porcentaje
        resultado[i] = resultado[i]/iterations * 100 
    return resultado

def calculatePercentage(output):
    graph = {}
    for i in output:
        if (len(i) > 0):
            for j in i:
                if (j in graph.keys()):
                    graph[j] = graph[j] + i[j]
                else:
                    graph[j] = i[j]
    for i in graph:
        graph[i] = graph[i] / len(output)
    return graph

# Recibe un grafo y aplica el algoritmo n veces. Luego hace la media de los porcentajes
def iteratePhaseAlgorithm(graph, rotation, iterations, nGraphs):
    output = []
    executer = qj.Drewom(extra={'return_struct':False})

    for _ in range(nGraphs):
        algoritmoFase = phaseAlgorithm(graph, rotation)
        circuito = executer.execute(algoritmoFase, iterations)
        output.append(frequency(circuito, iterations))

    return output

