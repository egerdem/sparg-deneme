
"""
Created on Fri Sep 14 04:31:00 2018

@author: Ege

Spherical harmonic constants' calculation

*Re-run this code if the "coeff" in directivity_6 is changed and update the bottom equation (if it results different than current one)

"""

from sympy import Symbol
from sympy import init_printing
from sympy import solve
from sympy import cos
from sympy import var
import numpy as np 
#import coeffs from directivity_6
#init_printing()
pi = np.pi

teta = var('teta')
a0, a1, a2, a3, a4 = var('a0 a1 a2 a3 a4')

#Y00 = np.sqrt(1/(4*pi))
#Y01 = np.sqrt(3/(4*pi))*cos(teta)
#Y02 = np.sqrt(5/(16*pi))*(3*(cos(teta)**2)-1)
#Y03 = np.sqrt(7/(16*pi))*(5*(cos(teta)**3)-3*cos(teta))
#Y04 =np.sqrt(9/(256*pi))*(35*(cos(teta)**4)-30*(cos(teta)**2)+3)

#E = a0*Y00 + a1*Y01 + a2*Y02 + a3*Y03 +a4*Y04

j = ( 0.282094791773878*coeffs[0] + 0.317356640745613*coeffs[4] - 0.31539156525252*coeffs[2] 
+ (0.48860251190292*coeffs[1] - 1.11952899777035*coeffs[3])*cos(teta)
+ (0.94617469575756*coeffs[2] - 3.17356640745613*coeffs[4])*cos(teta)**2
+ 1.86588166295058*coeffs[3]*cos(teta)**3  
+ 3.70249414203215*coeffs[4]*cos(teta)**4 )

#sols = solve([E1, E2, E3], [g1, g2, g3])

#print ("g1 = ", (sols[g1]).factor())
#print ("g2 = ", (sols[g2]).factor())
#print ("g3 = ", (sols[g3]).factor())
print(j)

""" re-run this code if the "coeff" in directivity_6 is changed and update the below equation
[ -9.53645370303659*cos(teta)**4 + 25.4758673956631*cos(teta)**3 
 - 25.6618252880878*cos(teta)**2 + 11.8788343768005*cos(teta) 
 - 1.4131367484532]
"""