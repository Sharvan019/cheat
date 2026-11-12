# PROGRAM-6: Quantum Superdense Coding Protocol
# Install first:  pip install qiskit qiskit-aer matplotlib

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

q = QuantumRegister(2, "q")
c = ClassicalRegister(2, "c")
qc = QuantumCircuit(q, c)

# Create entangled pair (Bell state)
qc.h(q[0])
qc.cx(q[0], q[1])

# Alice encodes the two classical bits (change message to 00, 01, 10 or 11)
message = "11"
if message == "00":
    pass
elif message == "01":
    qc.x(q[0])
elif message == "10":
    qc.z(q[0])
elif message == "11":
    qc.x(q[0])
    qc.z(q[0])
else:
    raise ValueError("Message must be 00, 01, 10, or 11")

# Bob decodes
qc.cx(q[0], q[1])
qc.h(q[0])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

print("Superdense Coding Circuit:")
print(qc.draw(output="text"))

simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts(qc)

print("Alice's encoded message:", message)
print("Bob's decoded measurement:", counts)

plot_histogram(counts)
plt.show()
