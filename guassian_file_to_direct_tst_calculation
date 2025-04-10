import re

a = 1.380649e-23  # Boltzmann constant (J/K)
b = 6.62607015e-34  # Planck constant (J·s)
c = 6.02214076e23  # Avogadro's number (mol^-1)
d = 2.99792458e10  # Speed of light in cm/s

def get_freqs(file):
    with open(file, 'r') as f:
        text = f.read()
    # Find all lines with 'Frequencies --'
    raw = re.findall(r"Frequencies --([\s\-0-9.]+)", text)
    freqs = []
    for block in raw:
        freqs += [float(x) for x in block.strip().split()]
    # Remove imaginary frequency (negative) for TS
    freqs = [f for f in freqs if f > 0.0]
    return freqs

t = float(input("Temperature (K): "))
e = float(input("Activation energy (kJ/mol): "))
e = e * 1000 / c  # convert to J per molecule

rf = input("Reactant log file: ")
tsf = input("TS log file: ")

x = get_freqs(rf)  # Reactant frequencies
y = get_freqs(tsf)  # TS frequencies

z = 1
for i in x:
    j = b * d * i
    z = z * (1 / (1 - 2.71828**(-j / (a * t))))

w = 1
for i in y:
    j = b * d * i
    w = w * (1 / (1 - 2.71828**(-j / (a * t))))

r = (a * t / b) * (w / z) * 2.71828**(-e / (a * t))
print("TST rate constant (s^-1):", r)
