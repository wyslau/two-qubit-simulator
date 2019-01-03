from __future__ import print_function

import numpy as np
from .quantum_gate import QuantumGate


class PhaseGate(QuantumGate):

    def __init__(self, *targets):

        phase_gate = np.array(
            [[1, 0], [0, np.exp(-1j * np.pi/4)]]
        ) / np.sqrt(2)

        if len(targets) == 1:
            operation = phase_gate
            symbol = u"Ru\u03A6"
        # Two qubit cheat version
        elif targets == (0, 1):
            operation = np.kron(np.eye(2), phase_gate)
            symbol = ["", u"Ru\u03A6"]
        elif targets == (1,0):
            operation = np.kron(phase_gate, np.eye(2))
            symbol = [u"Ru\u03A6", ""]
        else :
            raise TypeError(
                "Invalid targets: {}\n Should be of the form (1,), (0,1) or (1,0)".format(targets)
        )

        super(PhaseGate, self).__init__(operation, symbol)