
import numpy as np
from src.quantum_gates import QuantumGate
from src.quantum_state import QuantumState    

def test_quantum_state():
    qs1 = QuantumState(1)
    print(qs1.state_vector)
    qs1.apply_gate(QuantumGate.X(1), target_qubits=0)
    print(qs1.state_vector)
    print("------------------------------------------------------------")

    qs1.apply_gate(QuantumGate.Hadamard(1), target_qubits=0)
    print(qs1.state_vector)
    print("------------------------------------------------------------")
    qs2 = QuantumState(1)
    print(qs2.state_vector)
    qs2.apply_gate(QuantumGate.Hadamard(1), target_qubits=0)
    print(qs2.state_vector)

    print("------------------------------------------------------------")

    qs3 = QuantumState(2)
    print("Initial state vector:", qs3.state_vector)
    CNOT_matrix = QuantumGate.CNOT(2, control_qubit=0, target_qubit=1)
    qs3.apply_gate(CNOT_matrix, target_qubits=[0, 1])
    print("State vector after applying CNOT gate:", qs3.state_vector)
test_quantum_state()