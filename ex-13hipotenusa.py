from math import hypot
comCatOposto = float(input('comprimento do cateto oposto: '))
ComCatAdj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(comCatOposto, ComCatAdj)
print(f"A hipotenusa vai medir {hip:.2f}")