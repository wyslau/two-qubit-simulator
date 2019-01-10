from itertools import cycle, islice

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
        initial_state = np.zeros(2**n_qubits)
        initial_state[0] = 1

        for _ in range(n_rounds):

            random_circuit = QuantumCircuit()
            # Draw *n_gates* integers from a uniform distribution over the gate indices of the
            # gateset
            random_gate_indices = np.random.choice(
                [i for i in range(len(self.gate_set))], size=n_gates, replace=True
            )
            # Now extract the gates using the random indices
            random_gates = [self.gate_set[i] for i in random_gate_indices]


            # Why make this a generator in the first place? Circuit elements are defined as
            # lists in the QuantumCircuit class

            # Update (7/01)
            random_circuit.circuit_elements = random_gates

            # Undo the previous gate operations
            # Is this faster than actually calculating the recovery gate?
            # Also: implementation unelegant
            #for reverse_gate in random_gates[::-1]:
            #    random_circuit + reverse_gate # pylint: disable=pointless-statement


            # Update (7/01): Explicit calculation of recovery gate
            full_circuit_operation = np.linalg.multi_dot(
                [gate.unitary_operator for gate in random_gates]
            )
            recovery_gate = QuantumGate(np.linalg.inv(full_circuit_operation))

            random_circuit.circuit_elements.append(recovery_gate)

            # Assert that the gates multiply up to an identity
            assert np.allclose(
                np.linalg.multi_dot(
                    [op.unitary_operator for op in random_circuit.circuit_elements]
                    ),
                np.eye(2)
            )

            # Assert that all gates are unitary
            assert all(
                [
                    np.allclose(
                    g.unitary_operator.dot(np.conjugate(g.unitary_operator.T)),
                    np.eye(2)
                    ) for g in random_circuit.circuit_elements
                ]
            )
            qubit_register = QubitRegister(np.copy(initial_state))

            random_circuit.run_circuit(qubit_register)

            # Assert valid density operator
            assert np.allclose(qubit_register.state, np.conjugate(qubit_register.state.T))
            assert np.all(np.round(qubit_register.state, 8) >= 0)
            assert np.allclose(np.trace(qubit_register.state), 1)


            result = qubit_register.measure()

            if np.all(result == initial_state):
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
        QuantumGate(unitary_operator=c.dot(p)) for c in co_set for p in pauli_basis
    ]
    return clifford_gateset













