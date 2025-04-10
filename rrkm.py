b = 6.62607015e-34  # Planck constant
c = 6.02214076e23  # Avogadro number
d = 2.99792458e10  # speed of light

e = float(input("Ea (kJ/mol): "))  # energy threshold
e = e * 1000 / c  # convert to J per molecule

p = input("react freq: ")  # vibrational modes of reactant
q = input("ts freq (no imag): ")  # TS vibrational modes (no imaginary)

p = [float(i) for i in p.split()]
q = [float(i) for i in q.split()]

r = [b * d * i for i in p]  # convert to energy units (hv)
s = [b * d * i for i in q]

def g(x, y):
    # this counts the number of states with total energy ≤ x using a crude direct count
    from itertools import product
    z = 0
    u = [range(30) for _ in y]  # number of quanta per mode (limit to 30)
    for m in product(*u):  # all combinations
        n = sum([m[i]*y[i] for i in range(len(y))])  # total energy
        if n <= x:
            z += 1
    return z

ee = 1.1 * e  # arbitrary total energy
a1 = g(ee - e, s)  # numerator: sum of states in TS
a2 = g(ee, r)  # denominator: sum of states in reactant

# RRKM equation: k(E) = N‡(E - E0) / (h * ρ(E))
if a2 == 0:
    print("bad input")
else:
    k = a1 / (b * a2)
    print("rrkm k = ", k)
