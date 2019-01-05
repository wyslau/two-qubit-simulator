"""
Testing the qubit register class
"""

def test_qubit_initialisation():
    state = [[0],[1]]
    dmatrix = np.array([[0, 0],[0, 1]])
    register = QuantumRegister(state)
    assert dmatrix == register.state


def test_qubit_set_state():
	   


def test_qubit_unitary_rotation():
    
    pass