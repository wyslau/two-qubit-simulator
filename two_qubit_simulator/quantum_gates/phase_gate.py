from __future__ import print_function

import numpy as np
from .quantum_gate import QuantumGate


class PhaseGate(QuantumGate):

    def __init__(self, *targets, n_qubits=1):

        # Default to the first qubit
        if targets.__len__() == 0:
            targets = (0,)

        # In case somebody forgot to set n_qubits
        if n_qubits < len(targets):
            pass
            # raise an error 

        phase_gate = np.array(
            [[1, 0], [0, np.exp(-1j * np.pi/4)]]
        )

        phase_gate_symbol = u"Ru\u03A6"
        
        operation = 1
        symbol = []
        try:
            for i in range(n_qubits):
                if i in targets:
                    operation = np.kron(operation, phase_gate)
                    symbol.append(phase_gate_symbol)
                else:
                    operation = np.kron(operation, np.eye(2))
                    symbol.append('')
        except:
            raise TypeError(
                "Invalid targets: {}\n Should be of the form (1,), (0,1) or (1,0)".format(targets)
            )

        super(PhaseGate, self).__init__(operation, symbol)