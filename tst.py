a = 1.380649e-23  # Boltzmann constant (J/K)
b = 6.62607015e-34  # Planck constant (J·s)
c = 6.02214076e23  # Avogadro number (mol^-1)
d = 2.99792458e10  # speed of light (cm/s)

t = float(input("temp: "))  # temperature in K
e = float(input("Ea (kJ/mol): "))  # activation energy in kJ/mol
e = e * 1000 / c  # convert Ea to J per molecule

x = input("react freq: ")  # vibrational frequencies of reactant (cm^-1)
y = input("ts freq: ")  # vibrational frequencies of TS (excluding imaginary)

x = [float(i) for i in x.split()]  # convert to float list
y = [float(i) for i in y.split()]

z = 1
for i in x:
    j = b * d * i  # hv = h * c * v
    z = z * (1 / (1 - 2.71828**(-j / (a * t))))  # vibrational partition function for each mode

w = 1
for i in y:
    j = b * d * i
    w = w * (1 / (1 - 2.71828**(-j / (a * t))))

# TST equation: k = (k_B T / h) * (Q‡/Q) * exp(-Ea / (k_B T))
r = (a * t / b) * (w / z) * 2.71828**(-e / (a * t))
print("tst k = ", r)
