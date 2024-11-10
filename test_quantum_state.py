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

test_quantum_state()