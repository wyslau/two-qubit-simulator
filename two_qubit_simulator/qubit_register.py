"""
Contains the QubitRegister class
"""
from __future__ import division, print_function
import numpy as np


def conjugate_transpose(matrix):
    """ Calculates the conjugate transpose of a given matrix """
    return np.conjugate(matrix.transpose())


class QubitRegister(object): # pylint: disable=useless-object-inheritance
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

        # Cast to complex numpy array
        initial_state = np.array(initial_state).astype(np.complex128)

        # Test normalisation
        

        self.state = self._calculate_density_matrix_(initial_state)
        self.n_qubits = int(np.log(len(initial_state)) / np.log(2))

    def apply_unitary(self, unitary):
        unitary = unitary.astype(np.complex128)
        self.state = unitary.dot(self.state.dot(conjugate_transpose(unitary)))

    def _calculate_density_matrix_(self, state): # pylint: disable=no-self-use
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

    def measure(self, number_of_samples=1):
        # Always measures in Z
        #eig_vals, eig_vecs = np.linalg.eig(self.state)
        #outcome_probabilities = [np.sum(val**2 * vec) for val, vec in zip(eig_vals, eig_vecs)]

        # prepare basis projectors
        projectors = [
            self._calculate_density_matrix_(state_vector)
            for state_vector in np.eye(self.n_qubits * 2)
        ]
        outcome_probabilities = [
            np.abs(np.trace(projector.dot(self.state))) for projector in projectors
        ]

        results = np.random.choice([i for i in range(self.n_qubits * 2)],
            number_of_samples,
            p=outcome_probabilities)
        return [np.eye(self.n_qubits*2)[result, :] for result in results]
