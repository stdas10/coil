import math
from math import pi

#------FUNCTIONS------#



#------CONSTANTS------#

RO = 0.0172            # Copper resistivity 0.0172 Ohm*mm2/m
Imax = 4               # Max constant current for 1 mm2
k = 0.5                # Density coefficient
U = 220                # Voltage

#--------MAIN---------#
omega = 314
H = 15000 #int(input('Magnetic field in center, A/m: '))
D = 0.3 #float(input('Average diameter, m: '))

print(f'{D=}\n{H=}')

I_full = H * D

S_full = 2 * I_full / (Imax * 10**6)
d = S_full ** 0.5
r = D / 2

n = U / (D * H * ((RO * pi * Imax / H) + (0.01 * r**2 / (6*r + 19 * d))))

S = I_full / (Imax * n)
L = pi * D * n

Res = (RO * pi * n * D / S)
Xl = 314 * n**2 * 0.32 * 10**-4 *r**2 / (6*r + 19*d)

I = U / (Res + Xl)

print(f'Количество витков {n}')
      
print(f'Площадь сечения провода {S}\nДлина проволоки {L}\nСопротивление катушки {Res} {Xl}\nТок {I}')

