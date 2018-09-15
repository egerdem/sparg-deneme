
""" pattern coefficientlarını hesaplama """
#import pdb
import numpy as np

#import matplotlib.pyplot as plt
from scipy.special import sph_harm
from random_sample_triangle import rsp_sph

def degtorad(a):
    r = a*np.pi/180
    return r

def g(th,ph):
    g1 =  0.433100202347509*np.sin(degtorad(ph))*np.sin(degtorad(th)) + 0.700770847932726*np.cos(degtorad(th))
    return g1

""" Sample points and their corresponding teta & phi's """
teta,phi = zip(*rsp_sph)
lt = len(teta)
lp = len(phi)
p = len(phi)*len(teta)

count = 0
counter = 0

""" Gain matrix (via calculated formula g(t,f)) """
G = np.ones((p,1))
for t in range(lt):
    for f in range(lp):
         
        G[count]=g(teta[t],phi[f])
        count = count + 1
                
n = 25
C = np.zeros((p,n))
C = np.zeros((len(teta)*len(phi),n))

count_col = 0
count_row = 0

for t in range(lt):
    for f in range(lp):        
        for u in range(5):         
            for m in range(-u,u+1):
                if m<0:
                    C[count_row][count_col] = sph_harm(m, u, phi[f], teta[t]).imag
                elif m>=0:
                    C[count_row][count_col] = sph_harm(m, u, phi[f], teta[t]).real
                    
                count_col = count_col + 1
        count_col = 0
        count_row = count_row +1
        
Cpinv = np.linalg.pinv(C)

a = np.dot(Cpinv,G)
Gsaglama = np.dot(C,a)
print("a=\n",a)
