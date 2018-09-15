"""
Created on Fri Aug 10 00:09:18 2018

@author: Ege
"""
import numpy as np
import matplotlib.pyplot as plt
import random
from convertangle import cart2sph
from gains import Ls_row, Ls_col, t1
pi = np.pi

def point_on_triangle(L1, L2, L3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    s, t = sorted([random.random(), random.random()])
    return (s * L1[0] + (t-s)*L2[0] + (1-t)*L3[0],
            s * L1[1] + (t-s)*L2[1] + (1-t)*L3[1],
            s * L1[2] + (t-s)*L2[2] + (1-t)*L3[2])
    
sp_cart = []
sp_sph  = []
rsp_cart = []
rsp_sph = []
# rotate the 3 loudspeaker around the x axis, positive th_rotation is rotating it towards the positive z 
th_rotation_L1 = -(pi/2-t1)
th_rotation_z = t1
th_rotation = th_rotation_z
RTzy = np.array([[1,0,0],[0,np.cos(th_rotation),-np.sin(th_rotation)],[0,np.sin(th_rotation),np.cos(th_rotation)]])

for a in range(500):
    sample_points = point_on_triangle(Ls_row[0], Ls_row[1], Ls_row[2])
    sp_cart.append(sample_points)
    sp_sph.append(cart2sph(sample_points))
    
    
    rt_point_col = np.dot(RTzy,Ls_col)    
    rt_point_row =  rt_point_col.transpose()
    rt_sample_points = point_on_triangle(rt_point_row[0], rt_point_row[1], (rt_point_row[2]))
    rsp_cart.append(rt_sample_points)
    rsp_sph.append(cart2sph(rt_sample_points))
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#initial triangle
a, b, c = zip(*Ls_row)
x, y, z = zip(*sp_cart)

#rotated triangle
u, v, w = zip(*rt_point_row)
k, l, m = zip(*rsp_cart)


ax.scatter(a,b,c)
ax.scatter(x,y,z)
ax.scatter(u,v,w)
ax.scatter(k,l,m)
ax.scatter(0,0,0)


ax.set_ylim3d(-0.5,1.8)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
