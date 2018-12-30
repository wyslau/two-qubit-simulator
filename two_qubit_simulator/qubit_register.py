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
        pass

    def measure(self, basis):
        pass

    def apply_unitary(self, unitary):
        pass    

    def set_state(self, state):
        pass

    def _calculate_density_matrix_(self):
        pass

    def __repr__(self):
        print(self)