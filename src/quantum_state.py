import numpy as np
import random

class QuantumState:
    def __init__(self, number_of_qubits):
        self.number_of_qubits = number_of_qubits
        self.state_vector = np.zeros(2 ** number_of_qubits, dtype=complex)
        self.state_vector[0] = 1.0 # Initialize with |0> state
    
    def apply_gates(self, gates):
        for quantum_gate, target_qubits in gates:
            self.apply_single_gate(quantum_gate, target_qubits)
            print(f"State vector after applying {quantum_gate} to qubits {target_qubits}: {self.state_vector}")
            print("--------------------------------------------------------------------------------------------------")

    def lift_gate(self, gate, target_qubits):
        n = self.number_of_qubits
        num_targets = len(target_qubits)

        if gate.shape != (2 ** num_targets, 2 ** num_targets):
            raise ValueError(f"Gate matrix dimensions must be 2^{num_targets} x 2^{num_targets}")

        full_matrix = np.eye(2 ** n, dtype=complex)

        for idx in range(2 ** n):
            binary_idx = np.binary_repr(idx, width=n)
            target_bits = ''.join(binary_idx[q] for q in target_qubits)
            target_state_idx = int(target_bits, 2)

            for jdx in range(2 ** n):
                binary_jdx = np.binary_repr(jdx, width=n)
                if all(binary_idx[q] == binary_jdx[q] for q in range(n) if q not in target_qubits):
                    mapped_idx = int(''.join(binary_jdx[q] for q in target_qubits), 2)
                    full_matrix[idx, jdx] = gate[target_state_idx, mapped_idx]

        return full_matrix



    def apply_single_gate(self, quantum_gate, target_qubits):
        if isinstance(target_qubits, int):
            target_qubits = [target_qubits]
        target_qubits = sorted(target_qubits)
        lifted_gate = self.lift_gate(quantum_gate, target_qubits)
        self.state_vector = np.dot(lifted_gate, self.state_vector)

    def measure(self):
        probabilities = np.abs(self.state_vector) ** 2
        outcomes = list(range(len(probabilities)))
        measured_state = random.choices(outcomes, weights=probabilities, k=1)[0]
        return measured_state


    def __str__(self):
        return f"QuantumState({self.number_of_qubits} qubits): {self.state_vector}"
