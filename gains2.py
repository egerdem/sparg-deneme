"""
Comparison of gains obtained from closed form equation vs. numerical matrix calculation

"""
import numpy as np
from numpy import pi
from gains import Ls_row, t1, t2, t3, r

#sample angle to compare
teta = pi/2 # , polar angle
phi = pi/2 #, azimuth angle
t = teta
f = phi

# With Matrix Multiplication
p = (np.array([[np.sin(teta)*np.cos(phi)], [np.sin(teta)*np.sin(phi)], [np.cos(teta)]])) #virtual source unit vector
p_T = p.transpose()


L_inv = np.linalg.inv(Ls_row)  # inverse of loudspeaker pointing vectors

#gain vector
g=np.dot(p_T,L_inv)

#TETA1=np.array([np.arccos(np.dot(L1,p))])
#TETA2=np.array([np.arccos(np.dot(L2,p))])
#TETA3=np.array([np.arccos(np.dot(L3,p))])
#TETAS = np.concatenate((np.degrees(TETA1),np.degrees(TETA2),np.degrees(TETA3)))
#print("\nTETAS = ", TETAS)

# With Previously Obtained Formula
"""
Correct g1's, for triangle is in the front direction
g1_1 =  0.433100202347509*sin(f)*sin(t) + 0.700770847932726*cos(t)
g2_1 =  0.216550101173754*sin(f)*sin(t) - 0.666472681356099*sin(t)*cos(f) - 0.433100202347509*cos(t)
g3_1 =  0.216550101173754*sin(f)*sin(t) + 0.666472681356099*sin(t)*cos(f) - 0.433100202347509*cos(t)
"""
g1_1 =  -0.43310020235148*sin(f)*sin(t) - 6.06163851632283e-13*sin(t)*cos(f) + 0.700770847932726*cos(t)
g2_1 =  3.22719899462331e-15*(150043659398481.0*sin(f) - 206517380077430.0*cos(f))*sin(t)
g3_1 =  6.45439798924663e-16*(750218296989521.0*sin(f) + 1.03258690038925e+15*cos(f))*sin(t)


print("\ng = ", g , ": gain matris degerleri")

print('\ng =', g1_1, g2_1, g3_1, ": sembolik formülden") 

p_saglama = np.dot(g,Ls_row)
p_saglama = p_saglama.transpose()

#
#g_scaled = g/np.sqrt(g1_1**2+g2_1**2+g3_1**2)
#p_saglama = g_scaled*L123
#p_saglama = p_saglama.transpose()

