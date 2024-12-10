import numpy as np

class QuantumState:
    def __init__(self, number_of_qubits):
        self.number_of_qubits = number_of_qubits
        self.state_vector = np.zeros(2 ** number_of_qubits, dtype=complex)
        self.state_vector[0] = 1.0

    SWAP = np.array([[1, 0, 0, 0],
                     [0, 0, 1, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 1]])
    
    def apply_operator(matrix, column):
        return np.dot(matrix, column)
    
    def compose_operators(A, B):
        return np.dot(A, B)
    
    def apply_gate(self, state, gate, target_qubits):
        n = int(np.log2(gate.shape[0]))
        if len(target_qubits) != n:
            raise ValueError(f"Gate matrix dimensions must be 2^{len(target_qubits)} x 2^{len(target_qubits)}")
        
        if len(target_qubits) == 1:
            new_state = self.apply_one_quantum_gate(state, gate, target_qubits[0])
        else: 
            new_state = self.apply_n_quantum_gate(state, gate, target_qubits)
        
        return new_state
    
    def kronecker_product(self, A, B):
        return np.kron(A, B)
    
    def kronecker_exponential(self, A, n):
        if n<1:
            return np.ones(1,1)
        
        if n==1 
            return A
        else:
            return self.kronecker_product(A, self.kronecker_exponential(A, n-1))
        

    def lift_gate(self, gate, qubit, number_of_qubits):
        left = self.kronecker_exponential(np.identity, number_of_qubits - qubit - (int(np.log2(gate.shape[0]))))
        right = self.kronecker_exponential(np.identity, qubit)

        return self.kronecker_product(left, self.kronecker_product(gate, right))
        

    def apply_one_quantum_gate(self, state, gate, target_qubit):
        n = int(np.log2(state))
        return self.apply_operator(self.lift_gate(gate, target_qubit, n), state)  
    
    def permutations_to_transpositions(self, permutation):
        transpositions = []
        for dest in range(len(permutation)):
            src = permutation[dest]
            while src < dest:
                src = permutation[src]
            if src <  dest:
                transpositions.append((src, dest))  
            elif src > dest:
                transpositions.append((dest, src))
        return transpositions
    
    def transpositions_to_adj_transpositions(slef, transpositions):
        adj_transpositions = []
        for elements in transpositions:
            if elements[0] < elements[1]:
                adj_transpositions.extend([i for i in range(elements[0], elements[1])])
                adj_transpositions.extend([i for i in range(elements[1]-2, elements[0]-1, -1)])
        return adj_transpositions
    
    def apply_n_quantum_gate(self, state, gate, target_qubits):
        n = int(np.log2(state))
        def swap(i):
            return self.lift_gate(self.SWAP, i, n)
        def transposition_to_operator(transposition):
            if len(transposition) > 1:
                tmp = self.compose_operators(swap(transposition[0]), swap(transposition[1]))
                for i in range(2, len(transposition)):
                    tmp = self.compose_operators(tmp, swap(transposition[i]))
                return tmp
            elif len(transposition) == 1:
                return swap(transposition[0])   
            else:
                return self.kronecker_exponential(np.identity(2), n)
            
            