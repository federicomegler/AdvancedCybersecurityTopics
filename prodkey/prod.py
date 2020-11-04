import z3

x = z3.Int("x")
y = z3.Int("y")
z = z3.Int("z")


#z3.And(((x-0x30) == ((7-0x30) * 2 + 1))
# , (7 < x-0x30)) ,  (x == (x - (z-0x30)) + 2)


print( 732 + 4 & 0x3)