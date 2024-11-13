import numpy as np
import math

class QuantumGate:
    def __init__(self, matrix=None):
        if matrix is not None:
            self.matrix = matrix
        else:
            raise ValueError("A gate matrix must be provided")
        
    
    def X():
        X = np.array([[0,1],[1,0]], dtype=complex) # defining the X gate as the Pauli matrix
        return X
    
    def Y():
        Y = np.array([[0,-1j],[1j,0]]) # defining the Y gate as the Pauli matrix
        return Y
    def Z():
        Z = np.array([[1,0],[0,-1]])
        return Z
    
    def Hadamard():
        r = math.sqrt(2.0)
        H = np.array([[1/r,1/r],[1/r,-1/r]])
        return H
    
    def CNOT():
        CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex) # defining the CNOT gate
        return CNOT