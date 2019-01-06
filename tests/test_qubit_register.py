"""
Testing the qubit register class
"""
import numpy as np
from two_qubit_simulator import QubitRegister, Hadamard

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
    # Single qubit pure state
    qr_1 = QubitRegister([0, 1])
    assert np.allclose(qr_1.measure(number_of_samples=1), [0, 1])
    qr_2 = QubitRegister([1, 0])
    assert np.allclose(qr_2.measure(number_of_samples=1), [1, 0])

    # Measurement statistics
    # Apply the Hadamard gate to the qubit to create a maximally mixed state,
    # then measure the qubit state a large number of times and confirm the average
    # of state outcomes is 0.5
    had = Hadamard(0)
    had(qr_2)
    # Now gather measurement statistics
    num_samples = 1000
    average_outcome = np.sum([
        np.argmax(r) for r in qr_2.measure(number_of_samples=num_samples)
    ]) / num_samples

    delta = 0.05
    assert abs(average_outcome - 0.5) < delta

    # Two qubit tests
    qr_3 = QubitRegister([0, 0, 0, 1])
    assert np.allclose(qr_3.measure(number_of_samples=1), [0, 0, 0, 1])
    qr_4 = QubitRegister([0, 1, 0, 0])
    assert np.allclose(qr_4.measure(number_of_samples=1), [0, 1, 0, 0])
    


def test_qubit_unitary_rotation():
    
    assert False