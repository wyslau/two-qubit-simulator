from __future__ import print_function

import numpy as np
from .quantum_gate import QuantumGate

class Hadamard(QuantumGate):

    def __init__(self, *targets, n_qubits=1):

        # Default to the first qubit
        if targets.__len__() == 0:
            targets = (0,)

         # In case somebody forgot to set n_qubits
        if n_qubits < len(targets):
            pass
            # raise an error 

        hadamard_gate = np.array(
            [[1, 1], [1, -1]]
        ) / np.sqrt(2)

        hadamard_gate_symbol = "H"
        
        operation = 1
        symbol = []
        for i in range(n_qubits):
            if i in targets:
                operation = np.kron(operation, hadamard_gate)
                symbol.append(hadamard_gate_symbol)
            else:
                operation = np.kron(operation, np.eye(2))
                symbol.append('')

        super(Hadamard, self).__init__(operation, ["H",""])