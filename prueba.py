
import qsimov as qj
import numpy as np
from qsimov import QGate

# 2pi es 1 vuelta
def get_QFT(num_qubits):
    QFT = QGate(num_qubits, 0, f"QFT{num_qubits}")
    for i in range(num_qubits):
        QFT.add_operation("H", targets=[i])
        for j in range(num_qubits - i - 1):
            QFT.add_operation(f"RUnity({j+2})", targets=[i], controls={j+i+1})
    return QFT

##################### Código para crear un circuito cuántico simple ######################
# executer = qj.Drewom(extra={'return_struct':False})
# rotation = np.pi * 1 /4    
# gate = f'r({rotation})'  
# iterations = 10

# M1 = qj.QCircuit(4, 4, 'M1')       

# for i in range(4):
#     M1.add_operation('H', targets=i)    
    
# M1.add_operation(gate, targets=0,controls=1)     
# M1.add_operation(gate, targets=1,controls=2)
# M1.add_operation(gate, targets=0,controls=3)
# M1.add_operation(gate, targets=2,controls=3)
# M1.add_operation('measure', targets=[0,1,2,3], outputs=[0,1,2,3])   

# pr = executer.execute(M1, iterations)  



# print(pr)

# pr[iteracion][medida][qubit]

# iteracion = 0
# medida = 0
# qubit = 0


# resultado_0 = [pr[iteracion][0][0] for iteracion in range(10)]
# print(resultado_0)
# sum(resultado_0) / iterations   # iteraciones      La probabilidad medir 1

##############################################################

# executer = qj.Drewom()
# iteraciones = 1000

# iterations = 100

# pr = executer.execute(M1, iterations)  # Devuelve lista de mediciones por iteración

# pr[iteracion][medida][qubit]

# iteracion = 0
# medida = 0
# qubit = 0

# qb0 = [pr[i][0][0] for i in range(iterations)]
# qb0 = sum(qb0) / iterations
# print(qb0) # Prob de medir 1

##################################################################

# executer = qj.Drewom(extra={'return_struct':False})
# iteraciones = 1000

# # Circuito M1
# M1 = qj.QGate(5, 0, 'M1')
# rotacion = np.pi * 2 /8     # La rotación dependerá de qué tipo de puerta estemos usando 2/8 = ^1/4
# # z = f'rz({rotacion})'
# z = f'r({rotacion})'

# M1.add_operation(z, targets=0, controls=1)
# M1.add_operation(z, targets=0, controls=2)
# M1.add_operation(z, targets=0, controls=3)
# M1.add_operation(z, targets=1, controls=4)
# M1.add_operation(z, targets=2, controls=4)
# M1.add_operation(z, targets=3, controls=4)

# M1.add_operation('measure', targets=[0,1,2,3])
# # Execute devuelve el valor de los bits clásicos
# pr = executer.execute(M1, 10)
# print(pr)

# result = []
# for i in pr:
#     aux = []
#     for j in reversed(i):
#         if (j == True):
#             aux.append(1)
#         else:
#             aux.append(0)
#     result.append(aux)

# print(result)

# qb0 = [pr[i][0][0] for i in range(100)]
# qb0 = sum(qb0) / 100
# print(qb0)  # Prob de medir 1







# sum(resultado_0) / total iteraciones      La probabilidad medir 1

# executer = qj.Drewom()
# iteraciones = 1000

# # CIRCUITO M1
# M1 = qj.QCircuit(4, 'M1')


# for i in range(4):
#     M1.add_operation('H', targets=i)

# rotacion = np.pi * 2 /8
# z = f'rz({rotacion})'



# F1.add_operation('measure', [0,1,2,3])

# mediciones = executer.execute(F1, iteraciones)

# qb0 = [mediciones[i][0][0] for i in range(iteraciones)]
# qb0 = sum(qb0) / iteraciones

# qb1 = [mediciones[i][0][1] for i in range(iteraciones)]
# qb1 = sum(qb1) / iteraciones

# qb2 = [mediciones[i][0][2] for i in range(iteraciones)]
# qb2 = sum(qb2) / iteraciones

# qb3 = [mediciones[i][0][3] for i in range(iteraciones)]
# qb3 = sum(qb3) / iteraciones

# print(qb0)
# print(qb1)
# print(qb2)
# print(qb3)


# F1.add_operation(M1, targets=[0,1,2,3], controls=4)
# F1.add_operation(M1, targets=[0,1,2,3], controls=5)
# F1.add_operation(M1, [0,1,2,3], 5)
# F1.add_operation(M1, [0,1,2,3], 6)
# F1.add_operation(M1, [0,1,2,3], 6)
# F1.add_operation(M1, [0,1,2,3], 6)


# M1.add_operation('measure', [0,1,2,3])


# mediciones = executer.execute(M1, iteraciones)

# qb0 = [mediciones[i][0][0] for i in range(iteraciones)]
# qb0 = sum(qb0) / iteraciones

# qb1 = [mediciones[i][0][1] for i in range(iteraciones)]
# qb1 = sum(qb1) / iteraciones

# qb2 = [mediciones[i][0][2] for i in range(iteraciones)]
# qb2 = sum(qb2) / iteraciones

# qb3 = [mediciones[i][0][3] for i in range(iteraciones)]
# qb3 = sum(qb3) / iteraciones

# print(qb0)
# print(qb1)
# print(qb2)
# print(qb3)


# M1.add_operation(z, 0, 1)
# M1.add_operation(z, 1, 2)
# M1.add_operation(z, 0, 3)
# M1.add_operation(z, 2, 3)


