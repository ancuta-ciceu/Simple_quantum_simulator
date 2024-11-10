import numpy as np

class QuantumState:
    def __init__(self, number_of_qubits):
        self.number_of_qubits = number_of_qubits
        self.state_vector = np.zeros(2 ** number_of_qubits, dtype=complex)
        self.state_vector[0] = 1.0 #start in the state |0....0>


    def apply_gate(self, gate_matrix, target_qubits):
        if isinstance(target_qubits, int):
            target_qubits = [target_qubits]

        full_matrix = np.eye(1, dtype=complex)

        for qubit in range(self.number_of_qubits):
            if qubit in target_qubits:
                full_matrix = np.kron(full_matrix, gate_matrix)
            else:
                full_matrix = np.kron(full_matrix, np.eye(2, dtype=complex))

        self.state_vector = np.dot(full_matrix, self.state_vector)   
        
        def __str__(self):
            return f"QuantumState({self.number_of_qubits} qubits): {self.state_vector}"

print("i am in quantum_state.py")