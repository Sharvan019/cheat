# PROGRAM-2: Series Quantum Circuit Using Qiskit
# Install first:  pip install qiskit qiskit-aer matplotlib

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)
qc.x(0)
qc.h(0)
qc.z(0)
qc.measure(0, 0)

print("Series Quantum Circuit:")
print(qc.draw(output="text"))

simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
print("Measurement Results:", counts)

plot_histogram(counts)
plt.show()
