import qsimov as qj
import numpy as np
from qsimov import QGate
from qsimov.samples.fourier import get_swapped_QFT, get_QFT
import utils
import random 

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
    controlsCopy = controls.copy()
    ct = [i for i in range(len(controls))]

    # Creamos el circuito donde aplicar el algoritmo
    circuit = qj.QCircuit(nQubits, nBits, 'circuit')  

    # Aplicamos Hadamard a todos los qubits
    for i in range(nQubits):                    
        circuit.add_operation('H', i)

    nControls = len(controls)
    while (nControls != 0):    
        control = controlsCopy.pop() 
        for i in range(2**(nControls-1)):       
            # Aplicamos las puertas controladas M
            circuit.add_operation(oracle, targets=targets, controls=control)  
        nControls -= 1
    if exact:
        fourier = get_QFT(nBits)
    else:
        fourier = get_swapped_QFT(nBits) 
      
    # Aplicamos Fourier                             
    circuit.add_operation(fourier.invert(), targets=controls)     
    return circuit, controls, ct    # Devolvemos el circuito

def executeCircuit(matrix, simulator, iterations):
    executer = qj.Drewom(extra={'return_struct':simulator})
    cq, controls, ct = phaseAlgorithm(matrix, simulator)
    if simulator:
        circuit = executer.execute(cq, iterations=1)
        sys = circuit[0][0]
        nBits = cq.get_num_bits()
        nQubits = cq.get_num_qubits() - nBits
        prob = np.zeros(2**nBits)
        
        for i in range(2**nBits):
            aux = i * (2**nQubits) 
            for j in range(2**nQubits):
                val = sys.get_state(aux + j)
                prob[i] += val.real * val.real + val.imag * val.imag
        return utils.returnValues(prob)
    else:
        # Medimos         
        cq.add_operation('measure', targets=controls, outputs=ct) 
        circuit = executer.execute(cq, iterations=iterations)
        return utils.frequency(circuit, iterations)

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

# Lee un archivo en formato DIMACS y lo transforma en la matriz de adyacencia del grafo
def readGraphFile(file, node=None):
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

    m = utils.cutHalfMatrix(m)

    if (node is not None):
        m = utils.updateMatrix(m, node)
   
    return m

# VERSION COMO EN QUIRK
# Recibe un grafo, construye un circuito y devuelve los valores de la frecuencia
# def phaseAlgorithm(matrix, exact):
#     nQubits = len(matrix) + len(format(len(matrix), "b"))
#     rotacion = 0 # La rotación dependerá de qué tipo de puerta estemos usando 2/8 = ^1/4
#     for i in range(len(format(nQubits, "b")) + 1):
#         if (2**i >= nQubits):
#             rotacion = np.pi * 2/2**i  
#             break 
#     puerta = f'r({rotacion})'
#     # Creamos el Oráculo
#     oracle = getCircuit(matrix, puerta)  
#     nBits = len(format(len(matrix), "b"))
#     targets = [i for i in range(len(matrix))]
#     controls = [i + len(matrix) for i in range(len(format(len(matrix), "b")))]
#     ct = [i for i in range(len(controls))]

#     # Creamos el circuito donde aplicar el algoritmo
#     circuit = qj.QCircuit(nQubits, nBits, 'circuit')  

#     # Aplicamos Hadamard a todos los qubits
#     for i in range(nQubits):                    
#         circuit.add_operation('H', i)

#     nControls = len(controls)
#     indexControl = 0
#     while (nControls != 0):     
#         for i in range(2**indexControl):       
#             # Aplicamos las puertas controladas M
#             circuit.add_operation(oracle, targets=targets, controls=controls[indexControl])  
#         indexControl += 1
#         nControls -= 1
#     if exact:
#         fourier = get_QFT(nBits)
#     else:
#         fourier = get_swapped_QFT(nBits) 
      
#     # Aplicamos Fourier                             
#     circuit.add_operation(fourier.invert(), targets=controls)     
#     return circuit, controls, ct    # Devolvemos el circuito