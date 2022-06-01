import math, argparse, warnings
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, register

warning.filterwarnings("ignore")

max_quibits = 5
qx_url = "https://quantumexperience.ng.bluemix.net/d583c3f3cbf714354b85a93916cfc406bec15ee4b304b62d677db60910305c628d1f13f0d28b7d51bedc4fe522062d3b66a45a630e4a40fed64c75211cf6e439"

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument
