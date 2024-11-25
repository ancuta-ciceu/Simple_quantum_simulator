import numpy as np

class QuantumState:
    def __init__(self, number_of_qubits):
        self.number_of_qubits = number_of_qubits
        self.state_vector = np.zeros(2 ** number_of_qubits, dtype=complex)
        self.state_vector[0] = 1.0 # Initialize with |0> state
    
    def apply_gates(self, gates):
        for quantum_gate, target_qubits in gates:
            self.apply_single_gate(quantum_gate, target_qubits)

    def apply_single_gate(self, quantum_gate, target_qubits):

        if isinstance(target_qubits, int):
            target_qubits = [target_qubits]

        target_qubits = sorted(target_qubits)
        num_target_qubits = len(target_qubits)

    # Check if the gate matrix is valid for the number of target qubits
        if quantum_gate.shape != (2 ** num_target_qubits, 2 ** num_target_qubits):
            raise ValueError(f"Gate matrix dimensions must be 2^{num_target_qubits} x 2^{num_target_qubits}")

        full_matrix = np.eye(1, dtype=complex)
        qubit_idx = 0
        for qubit in range(self.number_of_qubits):
            if qubit_idx < num_target_qubits and qubit == target_qubits[qubit_idx]:
                if qubit_idx == 0:
                    full_matrix = np.kron(full_matrix, quantum_gate)
                qubit_idx += 1
            else:
                full_matrix = np.kron(full_matrix, np.eye(2, dtype=complex))

    
        expected_size = 2 ** self.number_of_qubits
        if full_matrix.shape[0] != expected_size:
            raise ValueError(f"Gate matrix size {full_matrix.shape[0]} does not match state vector size {expected_size}")


        self.state_vector = np.dot(full_matrix, self.state_vector)


    def __str__(self):
        return f"QuantumState({self.number_of_qubits} qubits): {self.state_vector}"
