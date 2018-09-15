# -*- coding: utf-8 -*-
"""
Dir için yeni bulunan katsayılarla pattern çizimi 
"""
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

def degtorad(a):
    r = a*np.pi/180
    return r

t0 = 2*180/5
t0 = degtorad(t0)

#WASPA Directivity Pattern Equation

def Dir(teta):
    #72,144,216,288,180 . 72 hariç 10 point
    #dir = -0.20060742+0.29687877*np.cos(teta)+1.12296062*np.cos(teta)**2+0.23524655*np.cos(teta)**3-0.42098147*np.cos(teta)**4-0.03079081*np.cos(teta)**5
    
    #benzetmek için 250 ve 170'e null koyunca :
    dir = -0.07585998-0.05853355*np.cos(teta)+0.8444851*np.cos(teta)**2+1.15553376*np.cos(teta)**3-0.27315687*np.cos(teta)**4-0.59900738*np.cos(teta)**5

    #144,216,180 null
    #dir = -0.13170743+0.15977812*np.cos(teta)+0.95148203*np.cos(teta)**2+0.58445511*np.cos(teta)**3-0.31923857*np.cos(teta)**4-0.24368949*np.cos(teta)**5
    
    #360-1,144,216,288,180
    #dir = -0.16009694+0.21258132*np.cos(teta)+1.02327175*np.cos(teta)**2+0.45109864*np.cos(teta)**3-0.36260193*np.cos(teta)**4-0.16311027*np.cos(teta)**5

    #144,216 null
    #dir = -0.10403335-0.00400746*np.cos(teta)+1.2005498*np.cos(teta)**2+0.67907079*np.cos(teta)**3-0.76429754*np.cos(teta)**4-0.00578851*np.cos(teta)**5
    
    #144,216,288,180 null
    #dir = -0.16088318+0.21534039*np.cos(teta)+1.02454411*np.cos(teta)**2+0.4433396*np.cos(teta)**3-0.36284343*np.cos(teta)**4-0.15786427*np.cos(teta)**5
    #dir = -0.2014006+0.29822803*np.cos(teta)+1.1251202*np.cos(teta)**2+0.23196072*np.cos(teta)**3-0.42239879*np.cos(teta)**4-0.02889897*np.cos(teta)**5
        
    #WASPA'daki KATSAYILAR
    #dir = -0.0402-0.0697*np.cos(teta)+0.6771*np.cos(teta)**2+1.2247*np.cos(teta)**3-0.1314*np.cos(teta)**4-0.6622*np.cos(teta)**5
    return dir

def Dirw(teta):
    """WASPA'daki KATSAILAR"""
    dir = -0.0402-0.0697*np.cos(teta)+0.6771*np.cos(teta)**2+1.2247*np.cos(teta)**3-0.1314*np.cos(teta)**4-0.6622*np.cos(teta)**5
    return dir

#Tangent Panning Law & Constant Sound Power

def T(a):
    T = ((np.tan(a)+np.tan(t0/2))/(np.tan(t0/2)-np.tan(a)))**2
    return T

def g(t):
    g = sqrt(T(t)/(1+T(t)))    
    return g

def D(t):
    d = np.sqrt(T(degtorad(36)-t)/(1+T(degtorad(36)-t)))    
    return d

print("formula gain = ", D(degtorad(50)))

print("pattern gain= ", Dir(degtorad(50)))

plt.figure(1)

tet = np.arange(0,2*np.pi,0.01)
teta = np.arange(0,2*np.pi/5,0.01)

ax = plt.polar(tet,Dir(tet),"-")
ax = plt.subplot(111, projection='polar')
#ax.set_rticks([0, 0.2, 0.4, 0.6, 0.8, 1])
ax.grid(True)
ax.set_title("With Coeffs", va='bottom')

ax = plt.polar(tet,Dirw(tet),"-")

#ax.set_title("Waspa", va='bottom')
plt.show()

f = []

for x in np.arange(0,2*np.pi,0.01):
    f.append(Dirw(x))
#    print(x*180/np.pi, Dirw(x))
