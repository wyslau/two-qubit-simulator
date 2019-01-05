from __future__ import print_function

import numpy as np
from .quantum_gate import QuantumGate


class PhaseGate(QuantumGate):

    def __init__(self, p_error, *targets):

         # Default to the first qubit
        if targets is None:
            targets = (0)

         # In case somebody forgot to set n_qubits
        if n_qubits < len(targets):
            pass
            # raise an error 

        gates = [
                eye(2),
                np.array(
                    [[0, 1], [1, 0]]
                ),
                np.array(
                    [[0, -1j], [1j, 0]]
                ),
                np.array(
                    [[1, 0], [0, -1]]
                )
            ]

        depolarising_gate_symbol = "E"
        
        self.operations = [1 - p_error , p_error / 3, p_error / 3, p_error / 3]
        symbol = []
        for gate, operation in zip(gates, operations):
        try:
            for i in range(n_qubits):
                if i in targets:
                    operation = kron(operation, hadamard_gate)
                    symbol.append(hadamard_gate_symbol)
                else:
                    operation = kron(operation, np.eye(2))
                    symbol.append('')
        except:
            raise TypeError(
                "Invalid targets: {}\n Should be of the form (1,), (0,1) or (1,0)".format(targets)
            )

        super(PhaseGate, self).__init__(operation, symbol)

        def __call__()