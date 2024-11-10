import numpy as np

# QuantumState class
class QuantumState:
    def __init__(self, number_of_qubits):
        self.number_of_qubits = number_of_qubits
        self.state_vector = np.zeros(2 ** number_of_qubits, dtype=complex)
        self.state_vector[0] = 1.0 # Initialize with |0> state

    def apply_gate(self, gate_matrix, target_qubits):
        # Ensure target_qubits is always a list of qubits
        if isinstance(target_qubits, int):
            target_qubits = [target_qubits]

        # Initialize the full matrix as identity matrix for no qubits
        full_matrix = np.eye(1, dtype=complex)

        # Build the full matrix using the Kronecker product
        for qubit in range(self.number_of_qubits):
            if qubit in target_qubits:
                full_matrix = np.kron(full_matrix, gate_matrix)  # Apply the gate
            else:
                full_matrix = np.kron(full_matrix, np.eye(2, dtype=complex))  # Apply identity to other qubits

        # Check if the matrix size matches the state vector size
        assert full_matrix.shape[0] == self.state_vector.shape[0], \
            f"Shape mismatch: full_matrix is {full_matrix.shape[0]} and state_vector is {self.state_vector.shape[0]}."

        # Apply the full gate matrix to the state vector
        self.state_vector = np.dot(full_matrix, self.state_vector)

    def __str__(self):
        return f"QuantumState({self.number_of_qubits} qubits): {self.state_vector}"
