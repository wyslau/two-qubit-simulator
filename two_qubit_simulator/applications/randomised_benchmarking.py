from itertools import cycle, islice
import random
import copy

import numpy as np
from two_qubit_simulator import QubitRegister, QuantumCircuit#, CNOT, Hadamard, PhaseGate



# Itertools round robin recipe
def splice(*iterables):
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
        Generates the Clifford gateset from the basic gates CNOT, Hadamard, Phase and
        Identity. For single-qubit gatesets we omit the CNOT gate.
    """
    #clifford_generators = [Hadamard(), PhaseGate(), np.eye(2)]













