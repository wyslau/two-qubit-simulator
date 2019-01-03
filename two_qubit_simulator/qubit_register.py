"""
Contains the QubitRegister class
"""
from __future__ import division, print_function
import numpy as np


class QubitRegister(object):
    """
        Defines a qubit register with one or two qubits.

        Parameters
        --------
            initial_state : list
                The initial qubit state as a vector

        Raises
        --------

    """

    def __init__(self, initial_state):
        self.state = self._calculate_density_matrix_(np.array(initial_state))
        self.n_qubits = int(np.log(len(initial_state)) / np.log(2))

    def __call__(self, unitary):
        self.apply_unitary(unitary)

    def apply_unitary(self, unitary):
        self.state = np.matmul(unitary, self.state, unitary.H)    

    def set_state(self, state):
        pass

    def _calculate_density_matrix_(self, state):
        return np.kron(state, state.H)

    def __repr__(self):
        print(self)