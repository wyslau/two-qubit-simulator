from __future__ import print_function
#import copy

import numpy as np
from .quantum_gate import QuantumGate


class Depolarising(QuantumGate):

    def __init__(self, p_error, *targets, n_qubits=1): # pylint: disable=super-init-not-called

         # Default to the first qubit
        if targets.__len__() == 0:
            targets = (0,)

         # In case somebody forgot to set n_qubits
        if n_qubits < len(targets):
            pass
            # raise an error 

        gates = [
                np.eye(2),
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
        for gate, operation_index in zip(gates, range(len(self.operations))):

            for i in range(n_qubits):
                if i in targets:

                    self.operations[operation_index] = np.kron(
                        self.operations[operation_index], gate
                    )
                    symbol.append(depolarising_gate_symbol)
                else:
                    self.operations[operation_index] = np.kron(
                        self.operations[operation_index], np.eye(2)
                        )
                    symbol.append('')


        self.symbol = symbol

    # This method needs to be fixed- registers is not defined (did you mean states)?
    #def apply_gate(self, registers):
    #    
    #    states = [copy.deepcopy(register) for i in len(self.operations)]
    #
    #    for state_index in enumerate(states): 
    #        states[state_index].apply_unitary(self.operations[state_index])
    #
    #    register.state = np.sum(register.state for register in registers)

