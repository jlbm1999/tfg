from types import MemberDescriptorType
import qsimov as qj
import numpy as np
from qsimov import QGate
import circuitos as ct
import grafos as gf
import time

inicio = time.time()

executer = qj.Drewom(extra={'return_struct':False})   # Calculo "realista"
# executer = qj.Drewom(extra={'return_struct':True})      # Valores Quirk
iteraciones = 1
nGrafos = 1
output = []

# Se introduce el grafo a mano desde la calse grafos.py
# m = gf.docMatrix 

# El grafo se lee desde el fichero DIMACS
m = ct.readGraphFile("grafos/sts/sts-13")


##################### PARA EJECUTAR EL CIRCUITO #####################
# Algoritmo de fase
algoritmoFase = ct.phaseAlgorithm(m)
circuito = executer.execute(algoritmoFase, iteraciones)
print(ct.frequency(circuito, iteraciones))
final = time.time()

##################### PARA EJECUTAR EL CIRCUITO #####################

# Circuito básico -> Ya se calcula en phaseAlgorithm()
# circuitoBasico = ct.getCircuit(m, puerta)

# Compara distintas ejecuciones del mismo grafo
# comparativaGrafos = ct.iteratePhaseAlgorithm(m, puerta, iteraciones, nGrafos)
# print(ct.calculatePercentage(comparativaGrafos))


# algoritmoFase = ct.phaseAlgorithm(m, puerta)
# circuito = executer.execute(algoritmoFase, 1)
# estadoCircuito = circuito[0][0].get_state()
# Cómo usar sys.prob(qubit_id)? -> recuerda quitar medida

print('La ejecución ha tardado ' + str(final-inicio) + ' segundos.')

