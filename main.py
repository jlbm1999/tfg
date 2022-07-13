import qsimov as qj
from qsimov import QGate
import circuitos as ct
import time
import utils

# Clase en la que se podrán ejecutar los experiemntos para el trabajo
# <>
exact = True
iterations = 10

inicio = time.time()
m = ct.readGraphFile("grafos/latin/latin-2")
cq = ct.executeCircuit(m, exact, iterations)
print(cq)
final = time.time()
print('La ejecución de STS-9 ha tardado ' + str(final-inicio) + ' segundos.')


# m1 = utils.prueba
# p = utils.permuteMatrix(utils.prueba2)
# print(m1)
# print(p)
# cq = ct.executeCircuit(m1, exact, iterations)
# print(cq)
# cq = ct.executeCircuit(utils.cutHalfMatrix(p), exact, iterations)
# print(cq)
# print('\n')

# pt = utils.petersen
# cq = ct.executeCircuit(pt, exact, iterations)
# print(cq)
# print('PETERSEN')
# print('\n')

# pr = utils.pentagonal
# cq = ct.executeCircuit(pr, exact, iterations)
# print(cq)
# print('PENTAGONAL')
# print('\n')

# cnt = 3
# for i in range(20):
#     inicio = time.time()
#     cq = ct.executeCircuit(utils.all_grahps[4], exact, iterations)
#     print(cq)
#     final = time.time()
#     print('La ejecución con ' + str(cnt) + ' nodos ha tardado ' + utils.timeConversion(final-inicio) + ' segundos.')
#     print('\n')
#     cnt += 1

# allM = utils.getAllMatrices(3)
# dic = {}
# for i in allM:
#     cq = ct.executeCircuit(i, exact, iterations)
#     if (str(cq) in dic.keys()):
#         dic[str(cq)] = dic[str(cq)] + 1
#     else:
#         dic[str(cq)] = 1
# print(dic)

