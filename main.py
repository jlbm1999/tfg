from types import MemberDescriptorType
import qsimov as qj
import numpy as np
from qsimov import QGate
import circuitos as ct
import grafos as gf

executer = qj.Drewom(extra={'return_struct':False})
iteraciones = 100
nGrafos = 1
output = []
rotacion = np.pi * 2 /8     # La rotación dependerá de qué tipo de puerta estemos usando 2/8 = ^1/4
puerta = f'r({rotacion})'
m = gf.prueba

# Circuito básico -> Ya se calcula en phaseAlgorithm()
# circuitoBasico = ct.getCircuit(m, puerta)

# Algoritmo de fase
algoritmoFase = ct.phaseAlgorithm(m, puerta)
circuito = executer.execute(algoritmoFase, iteraciones)
print(ct.frequency(circuito, iteraciones))

# Compara distintas ejecuciones del mismo grafo
# comparativaGrafos = ct.iteratePhaseAlgorithm(m, puerta, iteraciones, nGrafos)
# print(ct.calculatePercentage(comparativaGrafos))


