
"""
Symbolic Closed Form Gain Equation, only parametric

@author: Ege
"""

from sympy import Symbol

from sympy import init_printing

from sympy import solve

from sympy import sin,cos

from sympy import var

init_printing()
  
#t1 = Symbol('t1')
t1, t2, t3 = var('t1 t2 t3')
f1, f2, f3 = var('f1 f2 f3')
g1, g2, g3, r = var('g1 g2 g3 r')

t, f = var('t f')


L11 = r*sin(t1)*cos(f1)
L12 = r*sin(t1)*sin(f1)
L13 = r*cos(t1)

L21 = r*sin(t2)*cos(f2)
L22 = r*sin(t2)*sin(f2)
L23 = r*cos(t2)

L31 = r*sin(t3)*cos(f3)
L32 = r*sin(t3)*sin(f3)
L33 = r*cos(t3)

E1 = L11 * g1 + L21 * g2 + L31 * g3 - sin(t)*cos(f)
E2 = L12 * g1 + L22 * g2 + L32 * g3 - sin(t)*sin(f)
E3 = L13 * g1 + L23 * g2 + L33 * g3 - cos(t)

sols = solve([E1, E2, E3], [g1, g2, g3])

print ("g1 = ", (sols[g1]).factor())
print ("g2 = ", (sols[g2]).factor())
print ("g3 = ", (sols[g3]).factor())