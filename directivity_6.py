
""" pattern coefficientlarını hesaplama """

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from scipy.special import sph_harm,lpmv
from random_sample_triangle import rsp_sph, sp_sph

def g(th,ph):
    
    #Correct g1's, for triangle is in the front direction
    #g1 =  0.433100202347509*np.sin(ph)*np.sin(th) + 0.700770847932726*np.cos(th)
    
    #g1's if L1 towards head 
    g1 =  -0.43310020235148*np.sin(ph)*np.sin(th) - 6.06163851632283e-13*np.sin(th)*np.cos(ph) + 0.700770847932726*np.cos(th)
    return g1

teta,phi = zip(*rsp_sph)

lt = len(teta)
lp = len(phi)
p = len(phi)*len(teta)

count = 0
counter = 0

G = np.ones((p,1))
for t in range(lt):
    for f in range(lp):
         
        G[count]=g(teta[t],phi[f])
        count = count + 1
                
n = 5

C = np.zeros((len(teta)*len(phi),n))

for t in range(lt):
    for f in range(lp):        
        for n in range(5):
    
            C[counter][n] = sph_harm(0, n, phi[f], teta[t]).real
        
        counter = counter + 1
print("count" , count)
print("counter", counter)
Cpinv = np.linalg.pinv(C)

coeffs = np.dot(Cpinv,G)
print("coefficients =\n",coeffs)
Gsaglama = np.dot(C,coeffs)

plt.figure(2)
plt.plot(G)
plt.plot(Gsaglama)
