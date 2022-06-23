import circuitos as ct
import time
import utils

# Clase en la que se podrán ejecutar los experiemntos para el trabajo
# <>

#################### EXPERIMENTO 1 ####################
# Este experimento consiste en la creacion de 2 grafos aleatorios, donde se comprobara si son isomorfos o no (casi imposible)
# -> Se utilizara el metodo de medicion de simulador
exact = True
iterations = 1000
maxNodos = 16

# for i in range(maxNodos):
#     inicio = time.time()
#     for _ in range(1):
#         m = utils.randomMatrixGenerator(i + 1)
#         cq = ct.executeCircuit(m, exact, iterations)
#         print(cq)
#     final = time.time()
#     print('La ejecución con ' + str(i+1) + ' nodos ha tardado ' + utils.timeConversion(final-inicio) + ' segundos.')

#################### EXPERIMENTO 2 ####################
# En este experimento se creara un grafo aleatorio y su permutacion, y se comprobara si son isomorfos (100% tienen que serlo)
# -> Se utilizara el metodo de medicion de simulador



#################### EXPERIMENTO 3 ####################
# En este experimento se comprobará si el grafo de Petersen y el prisma pentagonal son isomorfos
# -> Se utilizara el metodo de medicion de simulador

cnt = 3
for i in utils.all_grahps:
    inicio = time.time()
    cq = ct.executeCircuit(i, exact, iterations)
    print(cq)
    final = time.time()
    print('La ejecución con ' + str(cnt) + ' nodos ha tardado ' + utils.timeConversion(final-inicio) + ' segundos.')
    print('\n')
    cnt += 1