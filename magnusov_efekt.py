from math import sqrt, sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt

'''
Welcome to the simulation of a baseball pitch. Computation is done considering gravitational, drag and magnus force and using simple euler integration method.
(This simulation is only aproximation of real world scenarion.)

RESULTS:
Acording to simulation, ball travels around 3m in direction which is horizontal and perpendiculary to the initial velocity, with given values.
This is not in agreement, with simulation done here: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/foilsimb/.
Similar results would be achieved, if the magnus force was smaller by factor of (2*pi).
As I don't have acces to their computation, I can not make further conclusions. However, 3m seams to be too much.

https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/aerodynamics-of-baseball/
'''

dt = 0.01                           # step size

# initialize parameters
rhov = 1.225                        # https://en.wikipedia.org/wiki/Density_of_air
g = np.array([0, 0, -9.81])
m = 0.149                           # https://en.wikipedia.org/wiki/Baseball_(ball)
v0 = 42.5                           # https://en.wikipedia.org/wiki/Fastball
phi = 5                             # angle between horizontal plane and velocity
s0 = np.array([0, 0, 1.8])
r = 0.038                           # https://en.wikipedia.org/wiki/Baseball_(ball)
c = 0.3                             # https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-on-a-baseball/
alpha = 0.5*c*rhov*(pi*r**2)        
omega0 = np.array([0, 0, 33*2*pi])  # https://www.drivelinebaseball.com/2016/11/spin-rate-what-we-know-now/
lc = 0.15                           # lift coeficient (https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/lift-of-a-baseball/)

# initialize fields to store position, velocity, aceleration
s = [s0]
v = [np.array([v0*cos(phi*2*pi/360), 0, v0*sin(phi*2*pi/360)])]
a = []
omega = [omega0]

# calculate throw considering gravitational, drag and magnus force
while True:
    a.append((g*m + lc*(4/3)*(pi**2)*(r**3)*rhov*4*np.cross(omega[0], v[-1]) - alpha*np.linalg.norm(v[-1])*v[-1])/m)
    s.append(s[-1] + v[-1]*dt)
    v.append(v[-1] + a[-1]*dt)
    if sqrt(s[-1][0]**2 + s[-1][1]**2) > 18.39 :
        break

# make lists to plot movement of ball in 3D
x, y, z = [], [], []
for i in s:
    x.append(i[0])
    y.append(i[1])
    z.append(i[2])

# print output
print(f"Distance traveled in in direction perpendicular to the plane defined by initial values is about {round(y[-1], 3)}m.")

# plot ball movement
ax = plt.axes(projection='3d')
ax.plot(x, y, z)

# set chart axes
ax.set_xlim(0, 19)
ax.set_ylim(0, 19)
ax.set_zlim(0, 19) 

# show chart
plt.show()


