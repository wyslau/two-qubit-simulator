"""
Contains the base class and all derived classes for 1 and 2 qubit gates

TODO:
    - implement all gates
    - make base class abstract with abc?

"""
from __future__ import division, print_function
import numpy as np

class QuantumGate(object):
    """
        Base class for a quantum gate

        Parameters
        ------------
            symbol : str, optional
                The symbol representing the gate. This is used when producing string
                representations of circuits.
            unitary_operator : numpy array
                The operator that implements the desired gate
    
        Raises
        -----------

    """

    def __init__(self, unitary_operator, symbol=None):
        self.symbol = symbol
        self.unitary_operator = unitary_operator.astype(np.complex128)

    # Apply the gate
    def __call__(self, register):
        """
            Apply the gate to a given qubit register

            Parameters
            ------------
                register : .qubit_register.QubitRegister
                    The register of qubits to which the gate is applied

            Returns
            ------------

            Raises
            ------------

        """

        register.apply_unitary(self.unitary_operator)

    def __repr__(self):
        """
            Print a representation of the gate using the class name and the symbol and
            unitary_operator attribute
        """
        return 'QuantumGate {} ({}):,\n'.format(
            self.__class__.__name__, self.symbol) + repr(self.unitary_operator)
