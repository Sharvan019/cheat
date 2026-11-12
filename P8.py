# PROGRAM-8: BB84 Quantum Key Distribution simulation
# Install first:  pip install qiskit qiskit-aer numpy

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

n_bits = 8
alice_bits = np.random.randint(2, size=n_bits)
alice_bases = np.random.randint(2, size=n_bits)
bob_bases = np.random.randint(2, size=n_bits)

simulator = AerSimulator()
bob_results = []

for i in range(n_bits):
    qc = QuantumCircuit(1, 1)
    if alice_bits[i] == 1:
        qc.x(0)          # encode bit
    if alice_bases[i] == 1:
        qc.h(0)          # Alice uses X basis
    if bob_bases[i] == 1:
        qc.h(0)          # Bob measures in X basis
    qc.measure(0, 0)
    result = simulator.run(transpile(qc, simulator), shots=1).result()
    bob_results.append(int(list(result.get_counts().keys())[0]))

bob_results = np.array(bob_results)

# Sifting: keep only positions where the bases match
matching_bases = alice_bases == bob_bases
alice_key = alice_bits[matching_bases]
bob_key = bob_results[matching_bases]

print(f"Alice's Bits:    {alice_bits}")
print(f"Alice's Bases:   {alice_bases}")
print(f"Bob's Bases:     {bob_bases}")
print(f"Bob's Results:   {bob_results}\n")
print(f"Shared Alice Key: {alice_key}")
print(f"Shared Bob Key:   {bob_key}")

if len(alice_key) > 0:
    qber = np.mean(alice_key != bob_key) * 100
    print(f"Key length: {len(alice_key)} of {n_bits} bits, QBER: {qber:.1f}%")

# Example circuit for one bit (X, H by Alice; H, measure by Bob)
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.h(0)
qc.barrier()
qc.h(0)
qc.measure(0, 0)
print(qc.draw("text"))
