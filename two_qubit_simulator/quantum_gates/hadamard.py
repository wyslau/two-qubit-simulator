from __future__ import print_function

import numpy as np
from .quantum_gate import QuantumGate

class Hadamard(QuantumGate):

    def __init__(self, *targets):

        hadamard_gate = np.array(
            [[1, 1], [1, -1]]
        ) / np.sqrt(2)

        if len(targets) == 1:
            operation = hadamard_gate
        # Two qubit cheat version
        elif targets == (0, 1):
            operation = np.kron(np.eye(2), hadamard_gate)
        elif targets == (1,0):
            operation = np.kron(hadamard_gate, np.eye(2))
        else :
            raise TypeError(
                'Invalid targets: {}\n Should be of the form 0,1 or 1,0'.format(targets)
        )

        super(Hadamard, self).__init__(operation, ["H",""])