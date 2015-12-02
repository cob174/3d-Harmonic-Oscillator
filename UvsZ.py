#3d harmonic oscillator
#andrew filiault
#michael chiong
#emilee conard

import math
import matplotlib.pyplot as pyplot

n=4.
epsilon=n+1.5
h=0.01
u0=0
u1=0.01
z=0.01
zmax=8.
l=0

zList=[0,h]
uList=[0,h**(l+1)]

#loop continues until z is greater than z max
while True:

  #radial equation with fixed incremented z
  u2=(2+(h**2.)*((0./(z**2.))+(0.25*(z**2.))-epsilon))*u1-u0
  z=z+h

  u0=u1
  u1=u2

  #normalization for plotting
  u2=u2**2.

  #plotting
  zList.append(z)
  uList.append(u2)

  #control structure to exit loops
  if zmax<z:
    break;

pyplot.plot(zList, uList)
pyplot.show()