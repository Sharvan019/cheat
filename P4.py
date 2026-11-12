# PROGRAM-4: Parallel Quantum Circuit
# Install first:  pip install qiskit

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)

print("Parallel Quantum Circuit:")
print(qc.draw(output="text"))

inputs = ["00", "01", "10", "11"]
for state in inputs:
    input_state = Statevector.from_label(state)
    output_state = input_state.evolve(qc)
    print("\nInput State:", state)
    print("Final Statevector:", output_state.data)
