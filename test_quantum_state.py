
import numpy as np
from src.quantum_gates import QuantumGate
from src.quantum_state import QuantumState    

def test_quantum_state():
    qs1 = QuantumState(3)
    print("Initial state vector:", qs1.state_vector)
    qs1.apply_gates([(QuantumGate.X(), [0]), (QuantumGate.Y(), [1]), (QuantumGate.Rx(2), [2])])
    print("State vector after applying gates:", qs1.state_vector)
    print("------------------------------------------------------------")

    qs3 = QuantumState(3)
    qs3.state_vector = np.array([1, 0, 0, 0, 0, 0, 0, 1], dtype=complex)

    print("Initial state vector:", qs3.state_vector)
    
    qs3.apply_gates([(QuantumGate.CNOT(),[0, 1])])
    print("State vector after applying CNOT gate:", qs3)

    print("------------------------------------------------------------")

    #qs4 = QuantumState(4)
    #qs4.state_vector = np.array([1, 0, 0, 1], dtype=complex)
    #print("Initial state vector:", qs4.state_vector)
    #qs4.apply_gate(QuantumGate.CNOT(), target_qubits=[0,1])
    #print("State vector after applying CNOT gate:", qs4.state_vector)
test_quantum_state()

