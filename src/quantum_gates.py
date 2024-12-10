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
        CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex) 
        return CNOT
    def I():
        I = np.array([[1,0],[0,1]], dtype=complex)
        return I
    
    def S():
        S = np.array([[1,0],[0,1j]], dtype=complex)
        return S
    
    def T():
        T = np.array([[1,0],[0,math.e**(1j*math.pi/4)]], dtype=complex)
        return T
    
    def Ph(delta):
        Ph = np.array([[math.e**(1j*delta),0],[0,math.e**(1j*delta)]], dtype=complex)
        return Ph
    
    def Rx(theta):
        Rx = np.array([[math.cos(theta/2),-1j*math.sin(theta/2)],[-1j*math.sin(theta/2),math.cos(theta/2)]], dtype=complex)
        return Rx
    
    def Ry(theta):
        Ry = np.array([[math.cos(theta/2),-math.sin(theta/2)],[math.sin(theta/2),math.cos(theta/2)]], dtype=complex)
        return Ry
    
    def Rz(theta):
        Rz = np.array([[math.e**(-1j*theta/2),0],[0,math.e**(1j*theta/2)]], dtype=complex)
        return Rz