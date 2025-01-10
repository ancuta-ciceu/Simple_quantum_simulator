'''
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
    qs3.apply_gates([(QuantumGate.CNOT(),[0, 2])])
    print("State vector after applying CNOT gate:", qs3)

    print("------------------------------------------------------------")

    qs4 = QuantumState(4)
    print("Initial state vector:", qs4.state_vector)
    qs4.apply_gates([(QuantumGate.Hadamard(), [0]), (QuantumGate.CNOT(), [1, 3])])
    print("State vector after applying CNOT gate:", qs4)

    print("------------------------------------------------------------")
test_quantum_state()

'''

import numpy as np
from src.quantum_state import QuantumState
from src.quantum_gates import QuantumGate
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow

quantum_state = QuantumState(3)
CNOT = QuantumGate.CNOT()  

circuit = [
    (QuantumGate.X(), 1),
    (CNOT, [1, 2]),
    (QuantumGate.X(), 0),
    (CNOT, [0, 1])
]

quantum_state.apply_gates(circuit)

print(f"Quantum state: {quantum_state}")

measured_state = quantum_state.measure()
print(f"Measured state: |{bin(measured_state)[2:].zfill(quantum_state.number_of_qubits)}⟩")

print("///////////////////////////////////////////////////////////////////////////")

quantum_state1 = QuantumState(3)
CNOT1 = QuantumGate.CNOT()  

circuit1 = [
    (QuantumGate.X(), 1),            
    (CNOT1, [2, 1]),      
    
]

quantum_state1.apply_gates(circuit1)

print(f"Quantum state: {quantum_state1}")

measured_state1 = quantum_state1.measure()
print(f"Measured state: |{bin(measured_state1)[2:].zfill(quantum_state1.number_of_qubits)}⟩")


print("///////////////////////////////////////////////////////////////////////////")

quantum_state2 = QuantumState(4)
CNOT2 = QuantumGate.CNOT()
Hadamard = QuantumGate.Hadamard()
NOT = QuantumGate.X()
circuit2 = [
    (Hadamard, 0),
    (CNOT2, [0, 1]),
    (Hadamard, 3),
    (CNOT2, [1, 3]),
    (NOT, 0),
    (Hadamard, 2),
    (Hadamard, 3),
    (CNOT2, [1, 2]),
    (Hadamard, 2),
    (CNOT2, [2, 1]),
    (CNOT2, [1, 0]),
    (Hadamard, 1),
]

quantum_state2.apply_gates(circuit2)

print(f"Quantum state: {quantum_state2}")

measured_state2 = quantum_state2.measure()
print(f"Measured state: |{bin(measured_state2)[2:].zfill(quantum_state2.number_of_qubits)}⟩")
