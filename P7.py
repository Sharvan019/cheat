# PROGRAM-7: Quantum Teleportation Protocol
# Install first:  pip install qiskit qiskit-aer matplotlib

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

q = QuantumRegister(3, "q")
c = ClassicalRegister(3, "c")
qc = QuantumCircuit(q, c)

# Alice prepares the state to teleport on qubit 0
theta = np.pi / 3
phi = np.pi / 4
qc.ry(theta, q[0])
qc.rz(phi, q[0])

# Entangle qubits 1 and 2
qc.h(q[1])
qc.cx(q[1], q[2])

# Alice's Bell measurement
qc.cx(q[0], q[1])
qc.h(q[0])
qc.measure(q[1], c[0])
qc.measure(q[0], c[1])

# Bob's corrections based on Alice's classical bits
with qc.if_test((c[0], 1)):
    qc.x(q[2])
with qc.if_test((c[1], 1)):
    qc.z(q[2])

# Undo the preparation on Bob's qubit to verify: it should measure 0
qc.rz(-phi, q[2])
qc.ry(-theta, q[2])
qc.measure(q[2], c[2])

print(qc.draw(output="text"))

simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
print("Measurement results:", counts)
# Leftmost bit is c[2]; it is always 0 when teleportation succeeds.

plot_histogram(counts)
plt.show()
