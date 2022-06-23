import qsimov as qj
from qsimov import QGate
import circuitos as ct
import time
import utils

# inicio = time.time()

# executer = qj.Drewom(extra={'return_struct':False})   # Calculo "realista"
executer = qj.Drewom(extra={'return_struct':True})      # Valores Quirk
exact = False
iterations = 1000
cutNode = None
# <>

# Grafos aleatorios
# m = ct.randomMatrixGenerator(5)
# print(m)

# Se introduce el grafo a mano desde la calse grafos.py
m = utils.prueba 
# m = ct.readGraphFile("grafos/latin/latin-2", cutNode)

# cq = ct.executeCircuit(utils.all_grahps[2], exact, iterations)
# print(cq)
# if (exact):
#     for i in range(len(cq)):
#         if (cq[i] > 10**(-25)):
#             print(str(i) + ': ' + str((cq[i] * 100).round(1)))
#         else:
#             print(str(i) + ': 0')
# else:
#     print(ct.frequency(cq, iterations))
    

# El grafo se lee desde el fichero DIMACS
# m = ct.readGraphFile("grafos/sts/sts-13")

# print(ct.executeCircuit(m, exact, iteraciones))

# algoritmoFase = ct.phaseAlgorithm(m)
# circuito = executer.execute(algoritmoFase[0], 1)
# sys, _ = circuito[0]
# odds = np.zeros(3)
# nBits = algoritmoFase[0].num_bits
# nQubits = algoritmoFase[0].num_qubits - nBits
# in_size = 2**nQubits
# out_size = 2**nBits

# for i in range(out_size):
#     aux = i << nQubits
#     for j in range(in_size):
#         val = sys.get_state(aux + j)
#         odds[i] += val.real * val.real + val.imag * val.imag
# print(odds)


##################### PARA EJECUTAR EL CIRCUITO #####################
# Algoritmo de fase
algoritmoFase = ct.phaseAlgorithm(utils.all_grahps[3], True)
circuito = executer.execute(algoritmoFase[0], 100)
print(circuito[0][0].get_state())
# final = time.time()

##################### PARA EJECUTAR EL CIRCUITO #####################

# Circuito básico -> Ya se calcula en phaseAlgorithm()
# circuitoBasico = ct.getCircuit(m, puerta)

# Compara distintas ejecuciones del mismo grafo
# comparativaGrafos = ct.iteratePhaseAlgorithm(m, puerta, iteraciones, nGrafos)
# print(ct.calculatePercentage(comparativaGrafos))


# algoritmoFase = ct.phaseAlgorithm(m)
# circuito = executer.execute(algoritmoFase, 1)
# sys, _ = circuito[0]
# odds = np.zeros(3)

# for i in range(3):
#     aux = i * 2**4
#     for j in range(16):
#         val = sys.get_state(aux + j)
#         odds[i] += val.real *  val.real + val.imag * val.imag
# print(odds)
# Cómo usar sys.prob(qubit_id)? -> recuerda quitar medida

# print('La ejecución ha tardado ' + str(final-inicio) + ' segundos.')

