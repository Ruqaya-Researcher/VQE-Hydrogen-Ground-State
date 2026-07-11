
from imports import *

# ======================================
# Build Ansatz
# ======================================

def build_ansatz(qubit_hamiltonian):

    ansatz = EfficientSU2(

        num_qubits=qubit_hamiltonian.num_qubits,

        reps=1,

        entanglement="linear"

    )

    initial_parameters = 2 * np.pi * np.random.random(

        ansatz.num_parameters

    )

    return ansatz, initial_parameters
