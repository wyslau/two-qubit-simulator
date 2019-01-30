"""
Contains the QubitRegister class
"""

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
        
        if not self.is_normalised:
            print('Warning! State not normalised!')
        assert self.dimension ==  (2,2) or self.dimension ==  (2,1)  , " Please enter a 1 or 2 qubit state"

        

    def apply_unitary(self, unitary):
        """ Apply a unitary state transformation on the qubit register """
        assert unitary @ unitary.conj().T == np.array([[1,0],[0,1]]), "Operator not unitary!"
        output =  unitary @ self.initial_state
        return output
        

    def measure(self, number_of_samples=1):
        """ Perform a measurement of the qubit register by sampling from a uniform
            probability distribution
        """
        pass




state1 = QubitRegister(np.array([[1,0],[0,1]]))
hadamard1 = Hadamard(2)
state.apply_unitary(hadamard1)