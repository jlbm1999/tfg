import circuitos as ct
import time
import utils

# Clase en la que se podrán ejecutar los experiemntos para el trabajo
# <>
exact = True
iterations = 1

#################### EXPERIMENTO 1 ####################
# Este experimento consiste en la creacion de 2 grafos aleatorios, donde se comprobara si son isomorfos o no (casi imposible)
# -> Se utilizara el metodo de medicion de simulador

# for i in range(2):
#     m = utils.randomMatrixGenerator(10, False)
#     print(m)
#     cq = ct.executeCircuit(m, exact, iterations)
#     print(cq)
#     print('GRAFO ' + str(i))
#     print('\n')

#################### EXPERIMENTO 2 ####################
# En este experimento se creara un grafo aleatorio y su permutacion, y se comprobara si son isomorfos (100% tienen que serlo)
# -> Se utilizara el metodo de medicion de simulador

m1 = utils.prueba
p = utils.permuteMatrix(utils.prueba2)
print(m1)
print(p)
cq = ct.executeCircuit(m1, exact, iterations)
print(cq)
cq = ct.executeCircuit(utils.cutHalfMatrix(p), exact, iterations)
print(cq)
print('\n')


#################### EXPERIMENTO 3 ####################
# En este experimento se comprobará si el grafo de Petersen y el prisma pentagonal son isomorfos
# -> Se utilizara el metodo de medicion de simulador

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


#################### EXPERIMENTO 4 ####################

# allM = utils.getAllMatrices(4)
# for i in allM:
#     print(i)
# for i in allM:
#     print(i)
#     cq = ct.executeCircuit(i, exact, iterations)
#     print(cq)

# <>


