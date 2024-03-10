import libnum
import gmpy2

p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)

e1 = 2333
e2 = 23333
m = "flag{I_l0ve_Y0u}"
m = libnum.s2n(m)
n = p * q
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)

print("n=", n)
print("c1=", c1)
print("c2=", c2)
print("e1=", e1)
print("e2=", e2)
