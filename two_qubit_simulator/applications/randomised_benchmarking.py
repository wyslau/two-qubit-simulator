import random
import copy
from two_qubit_simulator import QubitRegister, QuantumCircuit
from itertools import cycle, islice


# Itertools round robin recipe
def splice(*iterables):
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active > 0:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


class RandomisedBenchmarking(object):

    def __init__(self, gate_set, noise):
        self.gate_set = gate_set
        self.noise = noise


    def __call__(n_gates, n_qubits=1, n_rounds=100):
        
        results = [0, 0]
        recovered_result = np.zeros([0] * (2**n_qubits))
        recovered_result[0] = 1

        for _ in n_rounds:

            random_circuit = QuantumCircuit()
            random_elements = random.choices(gate_set, k=n_gates)
            
            circuit.circuit_elements = splice(random_elements, noise * n_gates)
            circuit.circuit_elements += random_elements.reverse()   # Undo the previous gate operations

            vec = copy.deepcopy(recovered_result)
            state = QubitRegister(vec)

            circuit.run(state)
            result = state.measure()

            if result == recovered_result:
                result[0] += 1
            else:
                resulse[1] += 1
        return results
            










