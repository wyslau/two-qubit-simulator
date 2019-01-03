from __future__ import print_function

import numpy as np
from .quantum_gate import QuantumGate

class CNOT(QuantumGate):

	def __init__(self, *targets):
		operation = None
		# Two qubit cheat version
		if targets == (0,1):
			operation = np.array([
				[1, 0, 0, 0],
				[0, 1, 0, 0],
				[0, 0, 0, 1],
				[0, 0, 1, 0]])
		elif targets == (1,0):
			operation = np.array([
				[1, 0, 0, 0],
				[0, 0, 0, 1],
				[0, 0, 1, 0],
				[0, 1, 0, 0]])
		else :
			# Raise an exception here
			print(" Invalid targets: {}\n Should be of the form 0,1 or 1,0".format(targets))

		# DIY for larger numbers of qubits
		super(CNOT, self).__init__(operation, [u"\u20dd",u"\u2022"])
