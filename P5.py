# PROGRAM-5: Three-qubit Fredkin gate (Controlled-SWAP)
# Install first:  pip install qiskit

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(3)
qc.cswap(0, 1, 2)  # control = qubit 0, targets = qubits 1 and 2

print("Fredkin Gate Circuit:")
print(qc.draw(output="text"))

inputs = ["000", "001", "010", "011", "100", "101", "110", "111"]
for state in inputs:
    input_state = Statevector.from_label(state)
    output_state = input_state.evolve(qc)
    print("\nInput:", state)
    print("Output:", output_state.to_dict())
    print("Statevector:", output_state.data)
