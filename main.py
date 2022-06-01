import math, argparse, warnings
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, register

warning.filterwarnings("ignore")

max_quibits = 5
qx_url = "https://quantumexperience.ng.bluemix.net/d583c3f3cbf714354b85a93916cfc406bec15ee4b304b62d677db60910305c628d1f13f0d28b7d51bedc4fe522062d3b66a45a630e4a40fed64c75211cf6e439"

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('max', metavar='n', type=int, nargs='?', default=16, help='a maximum integer to generate')
    parser.add_argument('--remote', action='store_true', default=False, help='run command on real remote quantum processor')
    parser.add_argument('--qx-token', nargs='?', help='api token for IBM Q Experience remote backend')
    args = parser.parse_args()

    if args.remote and args.qx_token is None:
        parser.error("--remote requires --qx token")

    next_power = next_power_of_2(args.max)
    if (next_power > args.max):
        print(f"Rounding input {args.max} to the next power of two: {next_power}")
        args.max = next_power


    return args


def next_power_of_2(n):
    return int(math.pow(2,math.ceil(math.log(n,2))))

def bit_from_counts(counts):
    return [k for k, v in counts.items() if v == 1][0]

def num_bits(n):
    return math.floor(math.log(n,2)) + 1

def get_register_sizes(n, max_quibits):
    register_sizes = [max_quibits for i in range(int(n/max_quibits))]
    remainder = n % max_quibits
    return register_sizes if remainder == 0 else register_sizes + [remainder]

def random_int(max, remote = False):
    bits = ''
    n_bits = num_bits(max-1)
    register_sizes = get_register_sizes(n_bits, max_quibits)
    backend = "ibmqx4" if remote else "local_qasm_simulator"

    for x in register_sizes:
        q = QuantumRegister(x)
        c = ClassicalRegister(x)
        qc = QuantumCircuit(x)

        qc.h(q)
        qc.measure(q,c)

        job_sim = execute(qc, backend, shots=1)
        sim_result = job_sim.result()
        counts = sim_result.get_counts(qc)


        bits += bit_from_counts(counts)

    return int(bits,2)

input = parse_input()

if input.remote:
    register(input.qx_token, qx_url)

result = random_int(input.max, input.remote)

print(result)
