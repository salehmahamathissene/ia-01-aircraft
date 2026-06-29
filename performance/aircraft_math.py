import math

g = 9.81
rho = 1.225

MTOW = 900
Vs = 60 / 3.6
CLmax = 1.6
AR = 8.5

W = MTOW * g

S = (2 * W) / (rho * Vs**2 * CLmax)

b = math.sqrt(AR * S)

c = S / b

WS = W / S

print("=" * 50)
print("IA-01 INITIAL DESIGN")
print("=" * 50)
print(f"Weight       : {W:.2f} N")
print(f"Wing Area    : {S:.2f} m²")
print(f"Wing Span    : {b:.2f} m")
print(f"Mean Chord   : {c:.2f} m")
print(f"Wing Loading : {WS:.2f} N/m²")
