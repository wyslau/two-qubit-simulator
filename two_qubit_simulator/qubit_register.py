"""
Contains the QubitRegister class
"""

class QubitRegister(object): # pylint: disable=useless-object-inheritance
    """ Defines a qubit register with one or two qubits.
        
        - - - WRITE DOCUMENTATION HERE - - -
    """

    def __init__(self, initial_state):
        """ Create a QubitRegister object """
        pass

    def apply_unitary(self, unitary):
        """ Apply a unitary state transformation on the qubit register """
        pass

    def measure(self, number_of_samples=1):
        """ Perform a measurement of the qubit register by sampling from a uniform
            probability distribution
        """
        pass

