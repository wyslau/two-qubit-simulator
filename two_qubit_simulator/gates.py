#
#  HERE BE DOCSTRINGS
#

class Gate(object):

	def __init__(self, symbol=None):
		self.symbol = symbol
		pass

	# Apply the gate
	def __call__(self, register):
		pass

	# Print the gate
	def __repr__(self):
		pass


class CNOT(Gate):

	def __init__(self):
		super(CNOT, self).__init__(symbol='CNOT')