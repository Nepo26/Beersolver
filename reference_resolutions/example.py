#************************************************************/
#                                                            /
# Cabeçalho ATIVIDADE 1 de programação                       /
#                                                            /
# Mecanica                                                   /
#                                                            /
# Curso de Engenharia                                        /
#                                                            /
# Professor José RIcardo Sabino                              /
#                                                            /
# Equipe:                                                    /
#                                                            /
# Nome 1, matricula                                          /
# NOme 2, matricula                                          /
# Nome 3, matricula                                          /
#                                                            /
# Problema 3.C5                                              /
#                                                            /
# Descrição breve do problema                                /
#                                                            /
# Descrição breve da solução matematica                      /
#                                                            /
# Incluir informações sobre a entrada de dados               /
#                                                            /
#************************************************************/
from random import random
import numpy as np

print(" ")
print("***************************************************")
print("*                                                 *")
print("*                       INICIO                    *")
print("*                                                 *")
print("***************************************************")
print(" ")
print("Vamos calcular para um número N de forças aplicadas")

N = 3
print("N = ", N)

print("A resultante não terá apenas componente y, ")
print("então podemos trabalhar com um vetor de")
print("três componentes: x, y e z, tipo float.")

Res = np.zeros(3)

print("Res = ", Res)

print("")
print("As dimensões do volume do espaço não foram")
print("dadas, vamos supor que seja L1 = L2 = L3 = 1.0")
L1 = 1.0
L2 = 1.0
L3 = 1.0
print("Dimensoes L1 = L2 = L3 = ", L1, L2, L3)

print("")
print("Vamos criar um array de números tipo float,")
print("chamado F, cada elemento desse array será ")
print("um vetor força no espaço.")
F = np.zeros((N,3))
print("")
print(F)
print(" ")
print("***************************************************")
print("*                                                 *")
print("*            DEFINIÇÃO DAS FORÇAS                 *")
print("*                                                 *")
print("***************************************************")
print(" ")

print("Forças aplicadas na barra, exemplo F[0] =", F[0])

print("")
print("Vamos criar outro array de números tipo float,")
print("chamado R, cada elemento desse array será ")
print("um vetor posição do vetor força sobre o espaço.")
print("")

R = np.zeros((N,3))
print("Posição das forças aplicadas na barra = \n")
print(R)

for i in range(N):
   for j in range(3):
      F[i, j] = 50.0*random()

print("Forças aplicadas no corpo:")
print("")
print(F)
print("")
for i in range(N):
   R[i, 0] = L1*random()
   R[i, 1] = L2*random()
   R[i, 2] = L3*random()

print(" ")
print("***************************************************")
print("*                                                 *")
print("*            DEFINIÇÃO DAS POSIÇÕES               *")
print("*                                                 *")
print("***************************************************")
print(" ")
print("Posição x das forças aplicadas no corpo")
print("")
print(R)

print("")
for i in range(N):
   Res[0] += F[i, 0]
   Res[1] += F[i, 1]
   Res[2] += F[i, 2]

print(" ")
print("***************************************************")
print("*                                                 *")
print("*            CÁLCULO DA FORÇA RESULTANTE          *")
print("*                                                 *")
print("***************************************************")
print(" ")
print("Resultante = ", Res)
print("")
print("Força Resultante Rx = ", "{:5.1f} N,".format(Res[0]))
print("Força Resultante Ry = ", "{:5.1f} N,".format(Res[1]))
print("Força Resultante Rz = ", "{:5.1f} N,".format(Res[2]))
print(" ")
print("***************************************************")
print("*                                                 *")
print("*           CÁLCULO DA MOMENTO RESULTANTE         *")
print("*                                                 *")
print("***************************************************")
print(" ")
print("")
print("Vamos calcular o produto vetorial, e obter")
print("o momento das forças, o vetor binário resultante")
print("")
print("Mx = Soma(yPz -zPy)), My = Soma(xPz -zPx) e Mz = Soma(xPy - yPx)")
print("")

Momento_Resultante_R = np.zeros(3)
print("Vetor Momento resultante inicializado: ", Momento_Resultante_R)

for i in range(N):
   Momento_Resultante_R[0] += R[i, 1]*F[i, 2] - R[i, 2]*F[i, 1]
   Momento_Resultante_R[1] += R[i, 0]*F[i, 2] - R[i, 2]*F[i, 0]
   Momento_Resultante_R[2] += R[i, 0]*F[i, 1] - R[i, 1]*F[i, 0]

print("Momento Resultante R = ", Momento_Resultante_R)

print("")
print("Momento Resultante Mx = ", "{:5.1f} N.m,".format(Momento_Resultante_R[0]))
print("Momento Resultante My = ", "{:5.1f} N.m,".format(Momento_Resultante_R[1]))
print("Momento Resultante Mz = ", "{:5.1f} N.m,".format(Momento_Resultante_R[2]))

print(" ")
print("***************************************************")
print("*                                                 *")
print("*              TESTE DE ORTOGONALIDADE            *")
print("*                                                 *")
print("***************************************************")
print(" ")

print("São perpendiculares? ")
print(" ")
print("Se sim, o produto escalar é nulo.")
print(" ")
print("Então vamos calcular e ver se vai dar zero:")
print(" ")
print("Fazendo o produto das compontentes Rx*Mx + Ry*My + Rz*Mz")
print(" ")
print(Res[0]*Momento_Resultante_R[0] + Res[1]*Momento_Resultante_R[1] + Res[2]*Momento_Resultante_R[2])
print(" ")
print("Fazendo uso da função vdot da numpy: ")
print("    np.vdot(Resultante, Momento_resultante)")
print(" ")
print(np.vdot(Res,Momento_Resultante_R))
print(" ")

if np.absolute(np.vdot(Res,Momento_Resultante_R)) > 0:
    print("Força e Momento não são ortogonais!")
else:
    print("Força e Momento são ortogonais")
print(" ")
print("***************************************************")
print("*                                                 *")
print("*                        FIM                      *")
print("*                                                 *")
print("***************************************************")
print(" ")
