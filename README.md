# Project design ideas


**Goal: Run RB on two-qubit simulator with different noises**

- Qubit class
    - number of qubits
    - apply unitary
    - measure state
    - set state
    
    
- Gates class
    - overload __call__ (qubit ) 
    - gate name attribute
    - gate type ( 1 or 2 qubit)
    - target

    
 - CNOT class(Gate)
 
- Noisy gate(Gate)
    


Ideas for the gates class:
    - Make Gates class abstract (abc)
    
    
- Circuits class (collection of gates)
    - overload `__call__` 
    - overload `__add__` to concatenate circuits
    - overload `__index__` to view individual gates


