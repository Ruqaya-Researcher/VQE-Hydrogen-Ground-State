
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.mappers import JordanWignerMapper

def build_hamiltonian():

    driver = PySCFDriver(
        atom="H 0 0 0; H 0 0 0.74",
        basis="sto3g",
        charge=0,
        spin=0,
        unit=DistanceUnit.ANGSTROM,
    )

    problem = driver.run()

    fermionic_hamiltonian = problem.hamiltonian.second_q_op()

    mapper = JordanWignerMapper()

    qubit_hamiltonian = mapper.map(fermionic_hamiltonian)

    return qubit_hamiltonian
