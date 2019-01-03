"""
Contains the QubitRegister class
"""
from __future__ import division, print_function
import numpy as np


def conjugate_transpose(matrix):
    """ Calculates the conjugate transpose of a given matrix """
    return matrix.transpose()


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
        self.state = self._calculate_density_matrix_(np.array(initial_state).astype(np.complex128))
        self.n_qubits = int(np.log(len(initial_state)) / np.log(2))

    def apply_unitary(self, unitary):
        unitary = unitary.astype(np.complex128)
        self.state = unitary.dot(self.state).dot(conjugate_transpose(unitary))

    def set_state(self, state):
        pass

    def _calculate_density_matrix_(self, state):
        # Check and adjust input dimension: need to have column vector
        dim = state.shape
        if len(dim) == 1:
            state = state[:, np.newaxis]
        elif len(dim) == 2:
            # Check that this is a column vector and not a matrix
            if dim[1] != 1:
                raise TypeError(
                    'Input state needs to be a vector, not matrix.'
                    + 'Got {} instead.'.format(state))
        else:
            raise TypeError(
                    'Input state needs to be a vector, not matrix.'
                    + 'Got {} instead.'.format(state))

        return np.kron(state, conjugate_transpose(state))

    def __repr__(self):
        return 'Quantum register with {} qubit{}, density matrix:\n'.format(
            self.n_qubits, 's' if self.n_qubits > 1 else ''
        ) + repr(self.state)