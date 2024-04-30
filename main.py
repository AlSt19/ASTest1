import numpy as np
from scipy.integrate import solve_ivp
L=1E-3
D=1E-9
c0=1E-4
c8=1
t0=0
t8=300
nt=20
t=np.linspace(t0,t8,nt)
nz=20
dz=L/nz
z=np.linspace(0,L+dz,nz+1)
cinit=c0*np.ones(nz+1)
cinit[-1]=c8

def ode(t,c):
    J=np.zeros_like(c)
    dc=np.diff(c)
    J[1:]=D*dc/dz
    J[0]=0
    dcdt=np.zeros_like(c)
    dcdt[:-1]=np.diff(J)/dz
    dcdt[-1]=0
    return dcdt

c=solve_ivp(ode,(t0,t8),cinit,t_eval=t)["y"]
print(t)

import matplotlib.pyplot as plt

fig,ax=plt.subplots()
ax.plot(z,c)
ax.set_xlabel("z/$m$")
ax.set_ylabel("c /$mol$ $m^{-3}$")

fig2,ax2=plt.subplots()
ax2.plot(t,c.T)
ax2.set_xlabel("t/$s$")
ax2.set_ylabel("c /$mol$ $m^{-3}$")

plt.show()

from mpl_toolkits import mplot3d
fig3 = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(c, t, z, 50, cmap='binary')
ax.set_xlabel('c')
ax.set_ylabel('t')
ax.set_zlabel('z')

