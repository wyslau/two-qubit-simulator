"""
Contains the QubitRegister class
"""

import numpy as np

class QubitRegister(object): # pylint: disable=useless-object-inheritance
    """ Defines a qubit register with one or two qubits.
        All members of the register class must be arrrys of shape (2,2) or (2,1)
        Non-normalised states can be initialised but will raise warnings

        Registers objects may have unitary operators assigned to them.
        Operators must be of shape (2,2)
        Operators must be normalised

    """

    def __init__(self, initial_state):
        self.dimension = initial_state.shape
        self.state = initial_state
        self.is_normalised = np.linalg.norm(self.state) == 1
        
        assert self.is_normalised, "State not Normalised!"
        assert self.dimension == (2,1)  , " Please enter a 1 qubit state"

        

    def apply_unitary(self, unitary):
        """ Apply a unitary state transformation on the qubit register """
        identity = np.array([[1,0],[0,1]])
        conj_transpose = unitary @ unitary.conj().T
        assert (conj_transpose == identity).all(), "Operator not unitary!"
        output =  unitary @ self.initial_state
        return output
        

    def measure(self, number_of_samples=1):
        """ Perform a measurement of the qubit register by sampling from a uniform
            probability distribution
        """
        pass


