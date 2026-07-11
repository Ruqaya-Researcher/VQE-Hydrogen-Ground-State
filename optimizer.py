
from imports import *

# ======================================
# Build Optimizer
# ======================================

def build_optimizer():

    optimizer_method = "COBYLA"

    optimizer_options = {

        "maxiter": 200,

        "disp": True

    }

    return optimizer_method, optimizer_options
