from z3 import *
import string


c0 = z3.Int('c0')
c1 = z3.Int('c1')
c2 = z3.Int('c2')
c3 = z3.Int('c3')
c4 = z3.Int('c4')
c5 = z3.Int('c5')
c6 = z3.Int('c6')
c7 = z3.Int('c7')
c8 = z3.Int('c8')
c9 = z3.Int('c9')
c10 = z3.Int('c10')
c11 = z3.Int('c11')
c12 = z3.Int('c12')


solver = z3.Solver()
solver.add((c0 ^ Int2BV(0x62,8)) != Int2BV(0x1b,8))


solver.check()

m = solver.model()
print(m)

