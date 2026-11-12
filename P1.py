# PROGRAM-1: To implement the qubits (single-qubit gates)
# Install first:  pip install qiskit qiskit-aer matplotlib

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = AerSimulator()


def run(qc, shots=1000):
    job = simulator.run(qc, shots=shots)
    return job.result().get_counts()


# 1. Simple circuit with only a measurement
qc = QuantumCircuit(1, 1)
qc.measure(0, 0)
print("Circuit with measurement only:")
print(qc)

# 2. Effect of individual gates on |0>
for gate in ["x", "y", "z", "s", "t", "h"]:
    qc = QuantumCircuit(1, 1)
    getattr(qc, gate)(0)
    qc.measure(0, 0)
    print(f"Gate {gate.upper()}: {run(qc)}")

# 3. Hadamard gate -> superposition, with histogram
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
counts = run(qc)
print("Hadamard counts:", counts)

plot_histogram(counts)
plt.show()
