from z3 import *
import string

c0 = z3.Int('c0')
c1 = z3.Int('c1')
c2 = z3.Int('c2')
c3 = z3.Int('c3')
c4 = z3.Int('c4')
c5 = z3.Int('c5')

solver = z3.Solver()
solver.add(c0 == 41 or c0 == 42)
solver.add(c1 == 41 or c1 == 42)
solver.add(c2 == 41 or c2 == 41)
solver.add(c3 == 41 or c3 == 42)
solver.add(c4 == 41 or c4 == 42)

solver.check()

m = solver.model()
string = ""
string += chr(m.eval(c0))
string += chr(m.eval(c2))
string += chr(m.eval(c3))
string += chr(m.eval(c4))
print(m)
