# PROGRAM-3: Creating a Bell state using Qiskit
# Install first:  pip install qiskit

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

print("Bell State Circuit:")
print(qc.draw(output="text"))

state = Statevector.from_instruction(qc)
print("\nFinal Statevector:")
print(state)

print("\nStatevector Amplitudes:")
print(state.data)
