"""
Contains the QuantumCircuit class
"""

class QuantumCircuit(object):

    def __init__(self):
        self.circuit_elements = []

    def add_gate(self, gate):
        self.circuit_elements.append(gate)

    def __add__(self, gate):
        self.add_gate(gate)

    def run_circuit(self, register):
        for gate in self.circuit_elements:
            gate(register)

    def __call__(register):
        run_circuit(register)
