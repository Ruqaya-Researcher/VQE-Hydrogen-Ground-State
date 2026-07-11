
from hamiltonian import build_hamiltonian
from ansatz import build_ansatz
from optimizer import build_optimizer
from estimator import build_estimator
from vqe import run_vqe

# ======================================
# Build Hamiltonian
# ======================================

hamiltonian = build_hamiltonian()

# ======================================
# Build Ansatz
# ======================================

ansatz, initial_parameters = build_ansatz(

    hamiltonian

)

# ======================================
# Build Optimizer
# ======================================

optimizer_method, optimizer_options = build_optimizer()

# ======================================
# Build Estimator
# ======================================

estimator = build_estimator()

# ======================================
# Run VQE
# ======================================

result = run_vqe(

    ansatz,

    hamiltonian,

    estimator,

    initial_parameters,

    optimizer_method,

    optimizer_options

)

# ======================================
# Final Energy
# ======================================

print("Ground State Energy =")

print(result.fun)
