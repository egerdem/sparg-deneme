#update 1
""" pattern coefficientlarını hesaplama """
#import pdb
import numpy as np

#import matplotlib.pyplot as plt
from scipy.special import sph_harm,lpmv
from random_sample_triangle import points

def degtorad(a):
    r = a*np.pi/180
    return r

    g1 =  1.0*(0.683281572999748*np.sin(degtorad(f))*np.sin(degtorad(t)) + 0.760845213036123*np.cos(degtorad(t)))
    return g1

""" Sample points and their corresponding teta & phi's """
teta,phi = zip(*points)
lt = len(teta)
lp = len(phi)
p = len(phi)*len(teta)

count = 0
counter = 0
#pdb.set_trace()

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
