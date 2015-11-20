#3d harmonic oscillator
#andrew filiault
#michael chiong
#emilee conard

import math
import matplotlib.pyplot as pyplot


zmax = 4 # iterations
n=1
l=0
h = 0.01



zList=[0,h]
uList=[0,h**(l+1)]
listofulist=[]
for l in range(0,6):
  epsilon = l+(3/2) # n+1/2
  zmax = 4 # iterations
  z=h
  vz=z*z/4
  u1=h**(l+1)
  u0=0
 
  

  while z<zmax:
    
    u2=(2+h*h*(l*(l+1)*z**(-2)+(z**2/4)-epsilon))*u1-u0
    
    # Save for plotting
    zList.append(z)
    uList.append(u2)


  # Shift for next iteration
    z=z+h
    u0= u1
    u1= u2
    l=l+1
  n=n+1  
  def square(uList):
    return [i**2 for i in uList]
  pyplot.plot(zList, square(uList))
  pyplot.show()
