from itertools import cycle, islice
import random
import copy

import numpy as np
from scipy.linalg import expm
from two_qubit_simulator import QubitRegister, QuantumCircuit, QuantumGate



# Itertools round robin recipe
def splice(*iterables):
    # alternative implementation (for two lists a and b): (j for i in zip(a, b) for j in i)  
    num_active = len(iterables)
    next_elements = cycle(iter(it).__next__ for it in iterables)
    while num_active > 0:
        try:
            for next_element in next_elements:
                yield next_element()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            next_elements = cycle(islice(next_elements, num_active))


class RandomisedBenchmarking(object): # pylint: disable=useless-object-inheritance

    def __init__(self, gate_set, noise):
        self.gate_set = gate_set
        self.noise = noise


    def __call__(self, n_gates, n_qubits=1, n_rounds=100):
        
        results = [0, 0]
        recovered_result = np.zeros([0] * (2**n_qubits))
        recovered_result[0] = 1

        for _ in n_rounds:

            random_circuit = QuantumCircuit()
            random_elements = random.choices(self.gate_set, k=n_gates)
            
            random_circuit.circuit_elements = splice(random_elements, self.noise * n_gates)
            # Undo the previous gate operations

            # Is this faster than actually calculating the recovery gate?
            random_circuit.circuit_elements += random_elements.reverse()

            vec = copy.deepcopy(recovered_result)
            state = QubitRegister(vec)

            random_circuit.run_circuit(state)
            result = state.measure()

            if result == recovered_result:
                results[0] += 1
            else:
                results[1] += 1
        return results

def create_single_qubit_gateset():
    """
        Generates the Clifford gateset from Pauli basis superimposed with a co-set, as
        defined in https://arxiv.org/pdf/1811.01920.pdf.
    """
    # Some useful functions for building gatesets
    x_rotation = lambda angle: expm( - 1j * angle / 2 * np.array([[0, 1],[1, 0]]))
    y_rotation = lambda angle: expm( - 1j * angle / 2 * np.array([[0, -1j],[1j, 0]]))
    z_rotation = lambda angle: expm( - 1j * angle / 2 * np.array([[1, 0],[0, -1]]))

    pauli_basis = [
        np.eye(2), x_rotation(np.pi), y_rotation(np.pi), z_rotation(np.pi)
    ]
    co_set = [
        np.eye(2),
        x_rotation(np.pi / 2), y_rotation(np.pi / 2), z_rotation(np.pi / 2),
        z_rotation(np.pi / 2).dot(x_rotation(np.pi / 2)),
        x_rotation(- np.pi / 2).dot(z_rotation(- np.pi / 2))
    ]

    clifford_gateset = [
        QuantumGate(unitary_operator=p.dot(c)) for p in pauli_basis for c in co_set
    ]
    return clifford_gateset













