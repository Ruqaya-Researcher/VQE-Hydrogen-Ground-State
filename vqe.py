
from imports import *

# ======================================
# Cost Function
# ======================================

def cost_function(

    parameters,

    ansatz,

    hamiltonian,

    estimator

):

    pub = (

        ansatz,

        [hamiltonian],

        [parameters]

    )

    result = estimator.run([pub]).result()

    energy = result[0].data.evs[0]

    return energy


# ======================================
# Run VQE
# ======================================

def run_vqe(

    ansatz,

    hamiltonian,

    estimator,

    initial_parameters,

    optimizer_method,

    optimizer_options

):

    result = minimize(

        cost_function,

        initial_parameters,

        args=(

            ansatz,

            hamiltonian,

            estimator

        ),

        method=optimizer_method,

        options=optimizer_options

    )

    return result
