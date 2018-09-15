
"""
Created on Fri Sep 14 03:57:17 2018

@author: Ege

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
#from directivity_6 import a

pi = np.pi
teta = np.arange(0,2*np.pi,0.01)

def Dir(teta):
    dir = coeffs[0]*sph_harm(0, 0, 0, teta)+coeffs[1]*sph_harm(0, 1, 0, teta)+coeffs[2]*sph_harm(0, 2, 0, teta)
    + coeffs[3]*sph_harm(0, 3, 0, teta)+coeffs[4]*sph_harm(0, 4, 0, teta)
    return dir

#Ymn
#Y00 = np.sqrt(1/(4*pi))
#Y01 = np.sqrt(3/(4*pi))*np.cos(teta)
#Y02 = np.sqrt(5/(16*pi))*(3*(np.cos(teta)**2)-1)
#Y03 = np.sqrt(7/(16*pi))*(5*(np.cos(teta)**3)-3*np.cos(teta))
#Y04 =np.sqrt(9/(256*pi))*(35*(np.cos(teta)**4)-30*(np.cos(teta)**2)+3)

D = ( 0.282094791773878*coeffs[0] + 0.317356640745613*coeffs[4] - 0.31539156525252*coeffs[2] 
+ (0.48860251190292*coeffs[1] - 1.11952899777035*coeffs[3])*np.cos(teta)
+ (0.94617469575756*coeffs[2] - 3.17356640745613*coeffs[4])*np.cos(teta)**2
+ 1.86588166295058*coeffs[3]*np.cos(teta)**3  
+ 3.70249414203215*coeffs[4]*np.cos(teta)**4 )

plt.figure(1)

ax = plt.polar(teta,D,"o")
ax = plt.polar(teta,Dir(teta),"o")
ax = plt.subplot(111, projection='polar')
#ax.set_rticks([0.25, 0.5, 0.75, 1])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line

ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')

plt.show()