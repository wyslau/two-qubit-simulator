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
        self.state = self._calculate_density_matrix_(np.array(initial_state).astype(np.float64))

    def measure(self, basis):
        pass


    def __call__(self, unitary):
        self.apply_unitary(unitary.astype(np.float64))

    def apply_unitary(self, unitary):
        self.state = np.matmul(unitary, self.state, conjugate_transpose(unitary))    

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
        print(self)