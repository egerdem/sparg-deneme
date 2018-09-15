
"""
Created on Thu Sep 13 21:08:31 2018

@author: ege

10 channels loudspeaker array such that 3 loudspeakers compose equilateral triangle
Thus, height is only dependent to the side of a pentagon
"""
import numpy as np

pi = np.pi
#side length of the pentagon, meter
a = 2
#center to vertices length, pentagon
r = 0.5*a/np.sin(np.radians(36)) 
t = np.sin(np.radians(54))*a/(2*np.sin(np.radians(36)))

#distance between top and bottom pentagons' centers, vertical height of the array
h = np.sqrt((a*np.sqrt(3)/2)**2-(a/(2*np.sin(np.radians(36)))-t)**2)

print(h)

t1 = np.arctan2(r,(h/2))
t2 = np.pi - t1
t3 = t2

f1, f2, f3 = pi/2, 7*pi/10, 3*pi/10

t1_deg, t2_deg, t3_deg = np.degrees(t1), np.degrees(t2), np.degrees(t3)

print("t1_rad = ",t1,"t1_deg = ", np.degrees(t1))
print("t2_rad = ",t2,"t2_deg = ", np.degrees(t2))
print("t3_rad = ",t3,"t3_deg = ", np.degrees(t3))

""" old ones
t1, t2, t3 = 3*pi/10, 7*pi/10, 7*pi/10
f1, f2, f3 = pi/2, 7*pi/10, 3*pi/10
"""

