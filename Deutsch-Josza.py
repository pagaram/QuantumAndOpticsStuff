import qiskit
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
from qiskit.visualization import visualize_transition, plot_histogram
import matplotlib.pyplot as plt
import numpy as np

#constant oracle
constant_oracle = qiskit.QuantumCircuit(2)
output = np.random.randint(2)

if output == 1:
    constant_oracle.x(1)

constant_oracle.draw('mpl')
plt.show()

#balanced oracle
balanced_oracle = qiskit.QuantumCircuit(2)
balanced_oracle.barrier()
balanced_oracle.cx(0, 1)
balanced_oracle.barrier()
balanced_oracle.x(0)

balanced_oracle.draw('mpl')
plt.show()

#creating dj circuit
dj_circuit = qiskit.QuantumCircuit(2,1)
dj_circuit.h(0)
dj_circuit.x(1)
dj_circuit.h(1)

dj_circuit.draw('mpl')
plt.show()

#now attaching oracle to circuit
oracle_fn = balanced_oracle
#oracle_fn = constant_oracle
dj_circuit = dj_circuit.compose(oracle_fn)

dj_circuit.draw('mpl')
plt.show()

#adding measurement
dj_circuit.h(0)
dj_circuit.barrier()
dj_circuit.measure(0,0)

dj_circuit.draw('mpl')
plt.show()

simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(dj_circuit).result()
counts = result.get_counts(dj_circuit)

plot_histogram(counts)
plt.show()




