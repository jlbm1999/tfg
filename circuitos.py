from types import MemberDescriptorType
import qsimov as qj
import numpy as np
from qsimov import QGate
from qsimov.samples.fourier import get_swapped_QFT, get_QFT

# Recibe un grafo, construye un circuito y devuelve los valores de la frecuencia
def phaseAlgorithm(matrix, exact):
    nQubits = len(matrix) + len(format(len(matrix), "b"))
    rotacion = 0 # La rotación dependerá de qué tipo de puerta estemos usando 2/8 = ^1/4
    for i in range(len(format(nQubits, "b")) + 1):
        if (2**i >= nQubits):
            rotacion = np.pi * 2/2**i  
            break 
    puerta = f'r({rotacion})'
    # Creamos el Oráculo
    oracle = getCircuit(matrix, puerta)  
    nBits = len(format(len(matrix), "b"))
    targets = [i for i in range(len(matrix))]
    controls = [i + len(matrix) for i in range(len(format(len(matrix), "b")))]
    ct = [i for i in range(len(controls))]

    # Creamos el circuito donde aplicar el algoritmo
    circuit = qj.QCircuit(nQubits, nBits, 'circuit')  

    # Aplicamos Hadamard a todos los qubits
    for i in range(nQubits):                    
        circuit.add_operation('H', i)

    nControls = len(controls)
    indexControl = 0
    while (nControls != 0):     
        for i in range(2**indexControl):       
            # Aplicamos las puertas controladas M
            circuit.add_operation(oracle, targets=targets, controls=controls[indexControl])  
        indexControl += 1
        nControls -= 1
    if exact:
        fourier = get_QFT(nBits)
    else:
        fourier = get_swapped_QFT(nBits) 
      
    # Aplicamos Fourier                             
    circuit.add_operation(fourier.invert(), targets=controls)     
    return circuit, controls, ct    # Devolvemos el circuito
# <>
def executeCircuit(matrix, exact, iterations):
    executer = qj.Drewom(extra={'return_struct':exact})
    cq, controls, ct = phaseAlgorithm(matrix, exact)
    if exact:
        circuit = executer.execute(cq, iterations=1)
        sys, _ = circuit[0]
        nBits = cq.get_num_bits()
        nQubits = cq.get_num_qubits() - nBits
        out_size = 2**nBits
        in_size = 2**nQubits
        odds = np.zeros(out_size)
        
        for i in range(out_size):
            aux = i << nQubits
            for j in range(in_size):
                val = sys.get_state(aux + j)
                odds[i] += val.real * val.real + val.imag * val.imag
        return odds
    else:
        # Medimos         
        cq.add_operation('measure', targets=controls, outputs=ct) 
        circuit = executer.execute(cq, iterations=iterations)
        return circuit

# Construye un circuito a partir de una matriz (no aplica Hadamard al principio)
def getCircuit(matrix, puerta):
    targets = []
    for i in range(len(matrix)):
        targets.append((i,[]))
        for j in range(len(matrix[i])):
            if (matrix[i][j] > 0):
                targets[i][1].append(j+i)

    oracle = qj.QGate(len(matrix), 0, 'oracle')
    for i in targets:
        while(len(i[1]) > 0):
            oracle.add_operation(puerta, targets=i[0], controls=i[1].pop(0))

    return oracle

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

# Recibe un grafo y aplica el algoritmo n veces. Luego hace la media de los porcentajes
def iteratePhaseAlgorithm(graph, rotation, iterations, nGraphs):
    output = []
    executer = qj.Drewom(extra={'return_struct':False})

    for _ in range(nGraphs):
        algoritmoFase = phaseAlgorithm(graph, rotation)
        circuito = executer.execute(algoritmoFase, iterations)
        output.append(frequency(circuito, iterations))

    return output

# Lee un archivo en formato DIMACS y lo transforma en la matriz de adyacencia del grafo
def readGraphFile(file):
    with open(file) as f: 
        lines = f.readlines()

    lines = [lines[i][2:-1] for i in range(len(lines))]
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
    nNodes = int(lines[0][1])    # Numero de nodos
    nEdges = int(lines[0][2])    # Numero de aristas

    edges = [(int(lines[i][0]) - 1, int(lines[i][1]) - 1) for i in range(1, nEdges + 1)]
    m = [[0 for _ in range(nNodes)] for _ in range(nNodes)]

    for i in edges:
        m[i[0]][i[1]] = 1

    count = 0
    for i in range(len(m)):
        m[i] = m[i][count:]
        count += 1
    
     # RECORDAR COMENTAR CUANDO NO HAGA FALTA
    m = updateMatrix(m, 1)
   
    return m

# Coge la matriz a la que se le ha eliminado el nodo y se eliminan los valores
def updateMatrix(matrix, index):
    matrix.pop(index)
        
    for i in range(index):
        for j in range(len(matrix[i])):
            if (j == index):
                matrix[i].pop(j)
    return matrix