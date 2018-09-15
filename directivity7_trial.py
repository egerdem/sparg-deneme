# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 23:40:03 2018

@author: ABRA A5
"""


""" pattern coefficientlarını hesaplama """

import numpy as np

#import matplotlib.pyplot as plt
from scipy.special import sph_harm,lpmv
from random_sample_triangle import points


count = 0
counter = 0

lt = 10
lp = 10
p = lt*lp

G = np.ones((p,1))
                
n = 25
C = np.zeros((p,n))
M = np.zeros((p,n))

count_col = 0
count_row = 0
count_colm = 0
for t in range(lt):
    for f in range(lp):        
        for u in range(5):         
            for m in range(-u,u+1):

                C[count_row][count_col] = u
                count_col = count_col + 1
                
                M[count_row][count_colm] = m
                count_colm = count_colm + 1
                
                
        count_col = 0
        count_colm = 0
        count_row = count_row + 1
        

Cpinv = np.linalg.pinv(C)

a = np.dot(Cpinv,G)
print("a=\n",a)

Gsaglama = np.dot(C,a)