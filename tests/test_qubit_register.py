"""
Testing the qubit register class
"""
import numpy as np
from two_qubit_simulator import QubitRegister

def test_qubit_initialisation():
    # Single qubit state
    qr_1 = QubitRegister([0, 1])
    assert np.allclose(qr_1.state, np.array([[0, 0], [0, 1]]))
    assert qr_1.n_qubits == 1
    # Two qubit state
    qr_2 = QubitRegister([0, 0, 0, 1])
    assert np.allclose(qr_2.state, np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]).astype(np.complex128))
    assert qr_2.n_qubits == 2



def test_qubit_measurement():
    pass

def test_qubit_set_state():
    pass

def test_qubit_unitary_rotation():
    pass