from random import random
import numpy as np

print("Vamos calcular a menor distancia do ponto E até linha DB")

lambda_AB = np.array([7/9, -4/9, 4/9])
print("Vetor unitário lambda_AB:",lambda_AB)

lambda_CD = np.array([-7/9, 4/9, -4/9])
print("Vetor unitário lambda_CD:",lambda_CD)

print("Produto escalar de lambda_AB e lambda_CD:",np.vdot(lambda_AB, lambda_CD))

r_A = np.array([0.0, 4, 96])
print("Vetor A: ", r_A)

r_C = np.array([120.0, 36.0, 100.0])
print("Vetor C: ", r_C)

r_E = np.array([90.0, 52.0, 0.0])
print("Vetor E: ", r_E)

A = 9.0
print("A é o comprimento da linha AB = A*lambda_AB = ", A)
C = 9.0
print("C é o comprimento da linha CD = C*lambda_CD = ", C)

r_B = A*lambda_AB + r_A
print("r_B = ", r_B)

r_D = C*lambda_CD + r_C
print("r_D = ", r_D)

r_DB = r_B - r_D
print("r_DB = ", r_DB)

r_DE = r_E - r_D
print("r_DE = ", r_DE)

print("ou também:")
r_BE = r_E - r_B
print("r_BE = ", r_BE)

lambda_DB = r_DB / np.sqrt(np.vdot(r_DB, r_DB))

print("lambda_DB =",lambda_DB)
print("Modulo de lambda_DB = ", np.vdot(lambda_DB, lambda_DB))
print("")
print("Distancia do ponto E à linha DB é lambda_DB x r_DE = lambda_DB x r_BE")

Linha_E = np.cross(lambda_DB, r_DE)
print("Vetor lambda_DB x r_DE =", Linha_E)

print("Vetor lambda_DB x r_BE =", np.cross(lambda_DB, r_BE))

print("Distancia do ponto E a linha DB =", np.sqrt(np.vdot(Linha_E, Linha_E)))

