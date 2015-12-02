#3d harmonic oscillator
#andrew filiault
#michael chiong
#emilee conard

import math
import matplotlib.pyplot as pyplot

n=2.
l=1.
epsilon=n+1.5
h=0.01
u0=0
u1=0.01**(l+1)
z=0.01
zmax=11.
r=.01
bigr=3.
c=2.
enot=2.

zList=[0,h]
uList=[0,h**(l+1)]

while True:
  z=r/.529

  #k=force constant of HCl in pm
  #radial equation depending on the value of r relative to R
  if r < bigr:
  	vr=.5*(.048/10**8)*(r**2)
  	u2=(2.+(h**2.)*(((l*(l+1))/(z**2.))+(vr/enot)-epsilon))*u1-u0

  if r == bigr:
  	vr=.5*(.048/10**8)*(r**2)
  	u2=(2.+(h**2.)*(((l*(l+1))/(z**2.))+(vr/enot)-epsilon))*u1-u0

  if r > bigr:
  	vr=.5*(.048/10**8)*(r**2)+c
  	u2=(2.+(h**2.)*(((l*(l+1))/(z**2.))+(vr/enot)-epsilon))*u1-u0
  
  #increment r and storage
  r=r+h
  u0=u1
  u1=u2

  #normalize values for plotting
  u2=u2**2.

  #plotting
  zList.append(r)
  uList.append(u2)

  #if z is more than z max, exit
  if zmax<z:
    break;

pyplot.plot(zList, uList)
pyplot.show()