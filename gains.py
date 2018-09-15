
from sympy import sin,cos
from sympy import init_printing
from sympy import var
from sympy import solve
import numpy as np
init_printing()
    
pi = np.pi

g1, g2, g3 = var('g1 g2 g3')
t, f = var('t f')

#side length of the pentagon, meter
a = 1.5

#center to vertices length, pentagon
l = 0.5*a/np.sin(np.radians(36)) 
dummy = np.sin(np.radians(54))*a/(2*np.sin(np.radians(36)))

#distance between top and bottom pentagons' centers, vertical height of the array
h = np.sqrt((a*np.sqrt(3)/2)**2-(a/(2*np.sin(np.radians(36)))-dummy)**2)

""" Loudspeaker Coordinates (spherical) , 1 above, 2 below left the center
 t,f // elevation (teta) and azimuth (phi) """

""" Original Loudspeaker Locations """
t1 = np.arctan2(l,(h/2))
t2 = np.pi - t1
t3 = t2

f1, f2, f3 = pi/2, 7*pi/10, 3*pi/10

""" L1 @Z, towards the head // Loudspeaker Locations """

#t1, f1 = cart2sph(rt_point_row[0])
#t2, f2 = cart2sph(rt_point_row[1])
#t3, f3 = cart2sph(rt_point_row[2])
#
t1, f1 = 0, 0
t2, f2 = 1.10714871779, 2.19911485751
t3, f3 = 1.10714871779, 0.942477796077

""" Loudspeaker Pointing Vectors """

r = 1.427
L1_x = r*np.sin(t1)*np.cos(f1)
L1_y = r*np.sin(t1)*np.sin(f1)
L1_z = r*np.cos(t1)
L1 = np.array([L1_x,L1_y,L1_z])

L2_x = r*np.sin(t2)*np.cos(f2)
L2_y = r*np.sin(t2)*np.sin(f2)
L2_z = r*np.cos(t2)
L2 = np.array([L2_x,L2_y,L2_z])

L3_x = r*np.sin(t3)*np.cos(f3)
L3_y = r*np.sin(t3)*np.sin(f3)
L3_z = r*np.cos(t3)
L3 = np.array([L3_x,L3_y,L3_z])

E1 = L1_x * g1 + L2_x * g2 + L3_x * g3 - sin(t)*cos(f)
E2 = L1_y * g1 + L2_y * g2 + L3_y * g3 - sin(t)*sin(f)
E3 = L1_z * g1 + L2_z * g2 + L3_z * g3 - cos(t)

sols = solve([E1, E2, E3], [g1, g2, g3])

print ("g1 = ", (sols[g1]))
print ("g2 = ", (sols[g2]))
print ("g3 = ", (sols[g3]))

""" loudspeaker vectors concatenated in 3x3 matrix """

Ls_row = np.array([L1,L2,L3])
Ls_col = Ls_row.transpose()

# Cartesian Coordinate vectors of loudspeakers if needed
#L1 = [r*np.sin(t1)*np.cos(f1), r*np.sin(t1)*np.sin(f1), r*np.cos(t1)]
#L2 = [np.sin(t2)*np.cos(f2), np.sin(t2)*np.sin(f2), np.cos(t2)]
#L3 = [np.sin(t3)*np.cos(f3), np.sin(t3)*np.sin(f3), np.cos(t3)]