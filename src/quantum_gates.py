import numpy as np
import math

class QuantumGate:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def X(n):
        X1 = np.array([[0,1],[1,0]])
        if n == 1:
            X =X1
        else:
            X = 1
            i = 1
            for i in range(1, n+1):
                X = np.kron(X, X1)
        return X
    
    def Y(n):
        Y1 = np.array([[0,-1j],[1j,0]]) # defining the Y gate as the Pauli matrix
        if n == 1:  #if n=1 then we simply return the Pauli matrix
            Y = Y1
        else: #otherwise we use the Kronecker product to get the !!tensor!! product of the Pauli matrix
            Y = 1
            i = 1
            for i in range(1, n+1):
                Y = np.kron(Y, Y1)
        return Y
    def Z(n):
        Z1 = np.array([[1,0],[0,-1]])
        if n == 1:
            Z = Z1
        else:
            Z = 1
            i = 1
            for i in range(1, n+1):
                Z = np.kron(Z, Z1)
        return Z
    
    def Hadamard(n):
        r = math.sqrt(2.0)
        H1 = np.array([[1/r,1/r],[1/r,-1/r]])
        if n == 1:
            H = H1
        else:
            H = 1
            i = 1
            for i in range(1, n+1):
                H = np.kron(H, H1)
        return H
    
print("i am in quantum_gate.py")